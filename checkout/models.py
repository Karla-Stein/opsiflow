import uuid
from django.db import models
from django_countries.fields import CountryField
from django.db.models import Sum

from profiles.models import UserProfile
from products.models import ProductOption

# Create your models here.

STATUS = ((0, "pending"), (1, "confirmed"), (2, "cancelled"), (3, "failed"))


class Order(models.Model):
    """
    An order model to store all checkout related user information as well as
    the payment ID and order status.
    """
    order_number = models.CharField(max_length=32, null=False,
                                    editable=False)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True,
                                     related_name='orders')
    user_first_name = models.CharField(max_length=50)
    user_last_name = models.CharField(max_length=50)
    user_email = models.EmailField()
    user_phone = models.CharField(max_length=25, blank=True)
    billing_address_1 = models.CharField(max_length=50)
    billing_address_2 = models.CharField(max_length=50,
                                         blank=True, null=True)
    billing_county = models.CharField(max_length=50,
                                      blank=True, null=True)
    billing_city = models.CharField(max_length=50)
    billing_postalcode = models.CharField(max_length=20, blank=True)
    billing_country = CountryField(blank_label='Country *')
    order_total = models.DecimalField(max_digits=10, decimal_places=2,
                                      null=False, default=0)
    payment_id = models.CharField(max_length=254, null=False, blank=False,
                                  default='')
    status = models.IntegerField(choices=STATUS, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Order number: {self.order_number}. Status: {self.status}'

    def update_total(self):
        self.order_total = (self.lineitems.aggregate
                            (Sum('lineitem_total'))
                            ['lineitem_total__sum']) or 0
        self.save()


class OrderLineItem(models.Model):
    """
    A model to store line item information, with product option,
    related orders and the total.
    """
    item_option = models.ForeignKey(ProductOption, on_delete=models.SET_NULL,
                                    null=True, blank=True,
                                    related_name='order_line_items')
    order = models.ForeignKey(Order, on_delete=models.CASCADE,
                              related_name='lineitems')
    quantity = models.PositiveIntegerField(default=1)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2,
                                         editable=False)

    def save(self, *args, **kwargs):
        self.lineitem_total = self.item_option.unit_price * self.quantity
        super().save(*args, **kwargs)
        self.order.update_total()
