from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from .models import Order, OrderLineItem
from products.models import ProductOption

import stripe
import json
import time


class StripeWebhookHandler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """

        intent = event.data.object
        print(intent)
        pid = intent.id
        bag = intent.metadata.bag
        user_profile = intent.metadata.user_profile
        save_details = intent.metadata.save_details

        # Get the Charge object
        stripe_charge = stripe.Charge.retrieve(
            intent.latest_charge
        )

        billing_details = stripe_charge.billing_details
        order_total = round(stripe_charge.amount / 100, 2)

        # Clean data in the shipping details
        for field, value in billing_details.address.to_dict().items():
            if value == "":
                billing_details.address[field] = None

        #  Check if order exists
        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.filter(payment_id=pid).first()
                if order:
                    order_exists = True
                    break
                else:
                    attempt += 1
                    time.sleep(1)
            except Exception as e:
                return HttpResponse(f'{e}',
                                    status=500)
            if not order:
                try:
                    full_name = billing_details.name
                    first_name = full_name.split()[0]
                    last_name = full_name.split()[1]
                    order = Order.objects.create(
                        # user_profile=user_profile,
                        user_first_name=first_name,
                        user_last_name=last_name,
                        user_email=billing_details.email or '',
                        user_phone=billing_details.phone or '',
                        billing_address_1=billing_details.address.line1 or '',
                        billing_address_2=(
                            billing_details.address.line2 or None),
                        billing_county=billing_details.address.state or None,
                        billing_city=billing_details.address.city or '',
                        billing_postalcode=(
                            billing_details.address.postal_code or ''),
                        billing_country=billing_details.address.country or '',
                        order_total=order_total,
                        payment_id=pid,
                        status=1,
                    )
                    print(f"WEBHOOK CREATED ORDER: {order.payment_id}")
                    for product_option_pk, quantity in (json.loads(bag)
                                                        .items()):
                        product_option = get_object_or_404(
                            ProductOption,
                            pk=product_option_pk)

                        order_line_item = OrderLineItem(
                            item_option=product_option,
                            order=order,
                            quantity=quantity,
                            )
                        order_line_item.save()
                except Exception as e:
                    return HttpResponse(
                        content=f'Webhook received:'
                        f'{event["type"]} | ERROR: {e}',
                        status=500)

        if order_exists:
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS:'
                f'Verified order already in database',
                status=200)

        return HttpResponse(
            content=f'Webhook received: {event["type"]}'
            f'SUCCESS Created order in webhook',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
