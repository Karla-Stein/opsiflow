from django.db import models
from django.core.exceptions import ValidationError

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
                                on_delete=models.CASCADE,
                                related_name='options')
    name = models.CharField(max_length=254)
    description = models.TextField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    fulfilment_choice = models.IntegerField(
        choices=FULFILMENT_CHOICE)
    download_file = models.FileField(null=True, blank=True,
                                     upload_to='downloads/')
    tier = models.IntegerField(
        choices=TIER, null=True, blank=True)
    delivery_days = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name

    def clean(self):
        # Raise error if custom workflow tier and fulfiment choice download was chosen.
        if self.fulfilment_choice == 0 and self.tier in [0, 1, 2]:
            raise ValidationError(
                "You can not select fulfilment choice download for tiered services")
        
        # Raise error if fullfilment choice is DIY Template but no
        # downloas was provided.
        if self.fulfilment_choice == 0 and not self.download_file:
            raise ValidationError("You must choose a file.")

        # Raise error if fullfilment choice is Set Up Service but
        # downloas was provided.
        if self.fulfilment_choice == 1 and self.download_file:
            raise ValidationError("You must not add a file.")

        # Raise error if fullfilment choice is Set Up Service but no
        # delivery days were provided.
        if self.fulfilment_choice == 1 and self.delivery_days is None:
            raise ValidationError("You must add delivery days.")

        # Raise error if fullfilment choice is DIY Template but
        # delivery days were provided.
        if self.fulfilment_choice == 0 and self.delivery_days:
            raise ValidationError("You must not add delivery days.")

        # Raise error if custom workflow tier was chosen but no
        # delivery days were provided.
        if self.tier in [0, 1, 2] and self.delivery_days is None:
            raise ValidationError("You must add delivery days.")



