from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm
from bag.contexts import bag_contents

import stripe

# Create your views here.


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Your bag is empty")
        return redirect(reverse('products'))

    current_bag = bag_contents(request)
    total = current_bag['grand_total']

    stripe_total = round(total * 100)

    order_form = OrderForm()
    return render(
        request,
        'checkout/checkout.html',
        {
            'order_form': order_form,
            'stripe_public_key': 'pk_test_51S8IkGCMM4bS9Chdf7mcqQYEupt3AVgzeVmfBCJ12K8C1bC8hTqp3Y7uRx4p23NcVZygnnHMvJFrb8xzOWtl7uZO00i1IACMTJ',
            'client_secret': 'test client secret',
        }
    )
