from django.shortcuts import render, get_object_or_404
from checkout.models import Order
from django.contrib import messages
from .models import UserProfile
from .forms import UserProfileForm

# Create your views here.


def purchases(request):

    orders = Order.objects.filter(
        user_profile=request.user.userprofile).order_by('-created_at')

    return render(
        request,
        'profiles/purchases.html',
        {'orders': orders}

    )


def my_profile(request):
    """
    A view to display the user profile
    """

    profile = get_object_or_404(UserProfile, user=request.user)
    form = UserProfileForm(instance=profile)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your Profile was updated')

    return render(
        request,
        'profiles/profile.html',
        {'profile': profile,
         'form': form}
    )
