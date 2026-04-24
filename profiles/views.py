from django.shortcuts import render, get_object_or_404, redirect
from checkout.models import Order
from django.contrib import messages
from django.contrib.auth import logout
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


def delete_account(request):
    """
    View to allow user to delete their account.
    """

    try:
        if request.method == 'POST':
            user = request.user
            logout(request)
            user.delete()

            messages.success(request, "Your account was successfully deleted")
            return redirect("/")

        messages.error(request,
                       "You have no permission to delete this account.")

        return redirect("/")

    except Exception as e:
        messages.error(request,
                       f'An error occured please try again.{e}')
        return redirect('my_profile/')
