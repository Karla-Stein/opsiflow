from django.contrib import admin
from .models import Category, Product, ProductOption


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'category',
        'name',
        'description',
    )

    # ordering = ('sku',)


class ProductOptionAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'name',
        'unit_price',
        'fulfilment_choice',
        'tier',
    )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductOption, ProductOptionAdmin)
