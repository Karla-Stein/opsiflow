from django.shortcuts import render
from .forms import OrderForm

# Create your views here.


def checkout(request):

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
