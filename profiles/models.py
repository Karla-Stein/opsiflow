from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField


class UserProfile(models.Model):
    """
    A user profile model for maintaining default
    billing information and order history.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_first_name = models.CharField(max_length=50, blank=True, null=True)
    default_last_name = models.CharField(max_length=50, blank=True, null=True)
    default_email = models.EmailField(max_length=20, null=True,
                                      blank=True)
    default_phone_number = models.CharField(max_length=20, null=True,
                                            blank=True)
    default_street_address1 = models.CharField(max_length=80, null=True,
                                               blank=True)
    default_street_address2 = models.CharField(max_length=80, null=True,
                                               blank=True)
    default_city = models.CharField(max_length=40, null=True,
                                    blank=True)
    default_county = models.CharField(max_length=80, null=True, blank=True)
    default_postcode = models.CharField(max_length=20, null=True, blank=True)
    default_country = CountryField(blank_label='Country *', null=True,
                                   blank=True)

    def __str__(self):
        return self.user.username
