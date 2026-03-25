from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category, ProductOption


# Create your views here.
def all_products(request):
    """
    A view to render all products
    """

    products = Product.objects.all()
    query = None
    categories = None

    # Filter products by category from navbar links
    if request.GET:
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

    return render(
        request,
        'products/products.html',
        {'products': products,
         'search_term': query,
         'current_categories': categories
         }
    )


def product_detail(request, pk):
    """
    A view to display product deatils and their options.
    """

    queryset = Product.objects.all()
    product = get_object_or_404(queryset, pk=pk)
    product_option = product.options.all()

    return render(
        request,
        'products/product_detail.html',
        {'product': product,
         'product_option': product_option}

    )
