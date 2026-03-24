from django.db import models

# Create your models here.


class Category(models.Model):
    # change name in admin panel
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category',
                                 on_delete=models.SET_NULL,
                                 related_name='product',
                                 null=True,
                                 blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    excerpt = models.TextField(max_length=240, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


FULFILMENT_CHOICE = ((0, "Download"), (1, "Service"))
TIER = ((0, "Starter"), (1, "Growth"), (2, "Pro"))


class ProductOption(models.Model):
    product = models.ForeignKey('Product',
                                on_delete=models.SET_NULL,
                                null=True,
                                blank=True,
                                related_name='options')
    name = models.CharField(max_length=254)
    description = models.TextField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    fulfilment_choice = models.IntegerField(
        choices=FULFILMENT_CHOICE, default=0)
    download_file = models.FileField(null=True, blank=True)
    tier = models.IntegerField(
        choices=TIER, null=True, blank=True)
    delivery_days = models.IntegerField(null=True, blank=True)
    max_modules = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name
