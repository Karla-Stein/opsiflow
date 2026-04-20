from django.shortcuts import render
from checkout.models import Order

# Create your views here.


def purchases(request):

    orders = Order.objects.filter(
        user_profile=request.user.userprofile).order_by('-created_at')

    return render(
        request,
        'profiles/purchases.html',
        {'orders': orders}

    )
