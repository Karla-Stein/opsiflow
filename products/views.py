from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from .models import Product


# Create your views here.
def all_products(request):
    """
    A view to render all products
    """

    products = Product.objects.all()
    query = None

    # enable keyword queries
    if request.GET:
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
         }
    )
