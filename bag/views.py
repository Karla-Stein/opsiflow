from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from products.models import ProductOption


# Create your views here.


def view_bag(request):
    """
    A view to return bag contents page
    """
    return render(
        request,
        'bag/bag.html'
    )


def add_to_bag(request):
    selected_option_pk = request.POST.get('selected_option_pk')
    selected_option = get_object_or_404(ProductOption,
                                        pk=selected_option_pk)
    redirect_url = request.POST.get('redirect_url')

    bag = request.session.get('bag', {})

    if selected_option_pk in list(bag.keys()):
        messages.warning(request, f'{selected_option} already in your bag')
    else:
        bag[selected_option_pk] = 1
        messages.success(request, f'{selected_option} was added to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)
