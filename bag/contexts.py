from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import ProductOption


def bag_contents(request):

    bag_items = []
    total = 0
    diy_count = 0
    product_count = 0
    bag = request.session.get('bag', {})

    # check items in bag
    for product_option_pk in bag.keys():
        product_count += 1
        product_option = get_object_or_404(ProductOption, pk=product_option_pk)
        total += product_option.unit_price
        if product_option.name == "DIY Template":
            diy_count += 1

        bag_items.append({
            'product_option': product_option,
        })

    if diy_count >= 3:
        bundle_discount = total * Decimal(settings.BUNDLE_DISCOUNT / 100)
    else:
        bundle_discount = 0

    grand_total = total - bundle_discount

    context = {
        'bag_items': bag_items,
        'diy_count': diy_count,
        'product_count': product_count,
        'bundle_discount': bundle_discount,
        'total': total,
        'grand_total': grand_total
    }

    return context
