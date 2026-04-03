from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.contrib import messages

from products.models import ProductOption


# Create your views here.


def view_bag(request):
    """
    A view to return bag contents page.
    """
    return render(
        request,
        'bag/bag.html'
    )


def add_to_bag(request):
    """
    View to add products to the bag.
    """
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


def remove_from_bag(request, pk):
    """
    View to remove items from the bag.

    **Context**:
    ``option_in_bag``:
        An instance of :model: `products.ProductOption`.
    """
    option_in_bag = get_object_or_404(ProductOption,
                                      pk=pk)
    bag = request.session.get('bag', {})
    pk = str(option_in_bag.pk)

    try:
        if pk in bag:
            bag.pop(pk)
            messages.success(request,
                             f'{option_in_bag.name} was removed from your bag')

        request.session['bag'] = bag
        return redirect('bag')

    except Exception as e:

        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
