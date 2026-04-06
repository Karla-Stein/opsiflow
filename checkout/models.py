from django.db import models
from profiles.models import UserProfile
from django_countries.fields import CountryField

# Create your models here.

STATUS = ((0, "pending"), (1, "confirmed"), (2, "cancelled"), (3, "failed"))


class Order(models.Model):
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
    status = models.IntegerField(choices=STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
