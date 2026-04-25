from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models import Min
from django.db.models.functions import Lower

from .models import Product, Category


# Create your views here.
def all_products(request):
    """
    A view to render all products
    """

    products = Product.objects.all()

    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey  # noqa

            # A - Z sorting
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            # Complexity Sorting by delivery days
            if sortkey == 'complexity':
                products = products.annotate(
                    complexity=Min('options__delivery_days'))
                sortkey = 'complexity'

            if sortkey == 'price':
                products = products.annotate(
                    price=Min('options__unit_price'))
                sortkey = 'price'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'asc':
                    sortkey = f'{sortkey}'
            products = products.order_by(sortkey)

        # Filter products by category from navbar links
        if 'category' in request.GET:
            categories = request.GET['category']
            products = products.filter(category__name=categories)
            categories = Category.objects.filter(name=categories)

        # Filter products by keyword from search bar
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "No search criteria entered!")
                return redirect(reverse('products'))

            # case insensitiv or logic
            queries = (Q(name__icontains=query) |
                       Q(description__icontains=query))
            products = products.filter(queries)

    products = products.annotate(min_price=Min('options__unit_price'),
                                 min_delivery=Min('options__delivery_days'))

    return render(
        request,
        'products/products.html',
        {'products': products,
         'search_term': query,
         'current_categories': categories,
         }
    )


def product_detail(request, pk):
    """
    A view to display product deatils and their options.
    """

    queryset = Product.objects.all()
    product = get_object_or_404(queryset, pk=pk)
    product_option = product.options.all()
    selected_option = product_option.first()

    return render(
        request,
        'products/product_detail.html',
        {'product': product,
         'product_option': product_option,
         'selected_option': selected_option}

    )
