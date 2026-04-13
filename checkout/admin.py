from django.contrib import admin
from .models import Order, OrderLineItem


class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'order_number',
        'created_at',
        'status',
    )


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderLineItem)
