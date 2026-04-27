from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.shortcuts import HttpResponse
from django.http import HttpResponseForbidden
from django.contrib import messages
from django.conf import settings
from django.http import JsonResponse
from django.http import FileResponse
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from .forms import OrderForm
from bag.contexts import bag_contents
from products.models import ProductOption
from .models import OrderLineItem, Order
from profiles.models import UserProfile

import stripe

# Create your views here.


def checkout(request):
    """
    A view to collect checkout data create the payment intent.
    Checkout data is saved to the session.
    """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':

        request.session['form_data'] = {
            'user_first_name': request.POST['user_first_name'],
            'user_last_name': request.POST['user_last_name'],
            'user_email': request.POST['user_email'],
            'user_phone': request.POST['user_phone'],
            'billing_address_1': request.POST['billing_address_1'],
            'billing_address_2': request.POST['billing_address_2'],
            'billing_county': request.POST['billing_county'],
            'billing_city': request.POST['billing_city'],
            'billing_postalcode': request.POST['billing_postalcode'],
            'billing_country': request.POST['billing_country'],
            'save_details': request.POST.get('save-details')
        }

        return JsonResponse({'success': True})

    try:
        profile = UserProfile.objects.get(user=request.user)
        order_form = OrderForm(initial={
            'user_first_name': profile.default_first_name,
            'user_last_name': profile.default_last_name,
            'user_email': profile.default_email,
            'user_phone': profile.default_phone_number,
            'billing_address_1': profile.default_street_address1,
            'billing_address_2': profile.default_street_address2,
            'billing_city': profile.default_city,
            'billing_county': profile.default_county,
            'billing_postalcode': profile.default_postcode,
            'billing_country': profile.default_country,
        })
    except UserProfile.DoesNotExist:
        order_form = OrderForm()

    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Your bag is empty")
        return redirect(reverse('products'))

    current_bag = bag_contents(request)
    total = current_bag['grand_total']

    stripe_total = round(total * 100)

    # create payment intent
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    if not stripe_public_key:
        messages.warning(request, "Stripe public key is missing.")

    return render(
        request,
        'checkout/checkout.html',
        {
            'order_form': order_form,
            'stripe_public_key': stripe_public_key,
            'client_secret': intent.client_secret,
        }
    )


def checkout_success(request):
    """
    A view to handle successful Stripe checkout, retrieve payment and
    order data, and associates OrderLineitem.
    Order and OrderLineItem is saved to the database and
    session cleared thereafter.
    """
    payment_intent = request.GET.get('payment_intent')
    bag = request.session.get('bag', {})
    checkout_data = request.session.get('form_data')

    # if not payment_intent or not bag or not checkout_data:
    #     messages.error(request, "Missing checkout data.")
    #     return redirect('checkout')

    order = Order.objects.filter(payment_id=payment_intent).first()

    if not order:
        order_form = OrderForm(checkout_data)

        if not order_form.is_valid():
            print(order_form.errors)
            messages.error(request,
                           "There was a problem with your order data.")
            return redirect('checkout')

        order = order_form.save(commit=False)
        order.payment_id = payment_intent
        order.status = 1
        order.user_profile = request.user.userprofile
        order.save()

        # Save user info
        save_details = checkout_data.get('save_details')
        if save_details:
            profile = request.user.userprofile

            profile.default_first_name = order.user_first_name
            profile.default_last_name = order.user_last_name
            profile.default_email = order.user_email
            profile.default_phone_number = order.user_phone
            profile.default_street_address1 = order.billing_address_1
            profile.default_street_address2 = order.billing_address_2
            profile.default_city = order.billing_city
            profile.default_county = order.billing_county
            profile.default_postcode = order.billing_postalcode
            profile.default_country = order.billing_country
            profile.save()

        for product_option_pk, quantity in bag.items():
            try:
                product_option = get_object_or_404(ProductOption,
                                                   pk=product_option_pk)

                order_line_item = OrderLineItem(item_option=product_option,
                                                order=order,
                                                quantity=quantity,
                                                )
                order_line_item.save()
            except ProductOption.DoesNotExist:
                messages.error(request, (
                    "This product option can't be found in our data base."
                    "Please contact us for assistance."
                ))

        order.update_total()

    # Send custom confirmation emails

    download_links = []

    for item in order.lineitems.all():
        if item.item_option.download_file:
            download_links.append({
                "name": item.item_option.product.name,
                "url": request.build_absolute_uri(
                    reverse("download", args=[item.pk])
                )
            })

    text_content = render_to_string(
        "checkout/emails/purchase_confirmation.txt",
        context={"order": order,
                 "download_links": download_links},
    )

    html_content = render_to_string(
        "checkout/emails/purchase_confirmation.html",
        context={"order": order,
                 "download_links": download_links},
    )

    msg = EmailMultiAlternatives(
        subject="Thank you for your Purchase",
        body=text_content,
        from_email=settings.EMAIL_HOST_USER,
        to=[order.user_email],
    )
    msg.attach_alternative(html_content, "text/html")
    msg.send()

    if 'bag' in request.session:
        del request.session['bag']
    if 'checkout_data' in request.session:
        del request.session['checkout_data']

    return render(
        request,
        'checkout/checkout_success.html',
        {'order': order}
    )


def download(request, pk):
    download = get_object_or_404(OrderLineItem, pk=pk)

    try:
        if request.user.userprofile == download.order.user_profile:
            if download.download_count > 0:
                download.download_count -= 1
                download.save()
                file = download.item_option.download_file
                return FileResponse(file.open(), as_attachment=True)
            else:
                messages.error(request,
                               'Your download count has reached its limit')
                return redirect('/')
        else:
            messages.error(request,
                           'No permission to download')
            return HttpResponseForbidden(status=403)

    except Exception as e:
        messages.error(request,
                       f'An error occured please try again or'
                       f' contact us: {e}')
        return HttpResponse(status=500)
