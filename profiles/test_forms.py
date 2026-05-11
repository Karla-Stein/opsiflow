from django.test import TestCase
from .forms import UserProfileForm


class TestUserProfileForm(TestCase):

    def test_default_email_is_valid(self):
        """Positive test for email field"""
        userprofile_form = UserProfileForm({
            'default_first_name': 'First Name',
            'default_last_name': 'Last Name',
            'default_email': 'email@address.com',
            'default_phone_number': 'Phone Number',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_county': 'County',
            'default_city': 'City',
            'default_postcode': 'Postal Code',
            'default_country': 'GB'
                                            })
        self.assertTrue(
            userprofile_form.is_valid(), msg='This is not an email')

    def test_default_email_is_invalid(self):
        """Negative test for email field"""
        userprofile_form = UserProfileForm({
            'default_first_name': 'First Name',
            'default_last_name': 'Last Name',
            'default_email': 'emailaddress.com',
            'default_phone_number': 'Phone Number',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_county': 'County',
            'default_city': 'City',
            'default_postcode': 'Postal Code',
                                            })
        self.assertFalse(
            userprofile_form.is_valid(), msg='Email input is correct')

    def test_default_country_is_valid(self):
        """Positive test for Country field"""
        userprofile_form = UserProfileForm({
            'default_first_name': 'First Name',
            'default_last_name': 'Last Name',
            'default_email': 'email@address.com',
            'default_phone_number': 'Phone Number',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_county': 'County',
            'default_city': 'City',
            'default_postcode': 'Postal Code',
            'default_country': 'GB'
                                            })
        self.assertTrue(
            userprofile_form.is_valid(),
            msg='Default country is not a country code')

    def test_default_country_is_invalid(self):
        """Negative test for Country field"""
        userprofile_form = UserProfileForm({
            'default_first_name': 'First Name',
            'default_last_name': 'Last Name',
            'default_email': 'email@address.com',
            'default_phone_number': 'Phone Number',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_county': 'County',
            'default_city': 'City',
            'default_postcode': 'Postal Code',
            'default_country': 'United Kingdom'
                                            })
        self.assertFalse(
            userprofile_form.is_valid(),
            msg='Default country is a country code')

    def test_empty_form_is_valid(self):
        """Positive test for all fields being non required"""
        userprofile_form = UserProfileForm({
            'default_first_name': '',
            'default_last_name': '',
            'default_email': '',
            'default_phone_number': '',
            'default_street_address1': '',
            'default_street_address2': '',
            'default_county': '',
            'default_city': '',
            'default_postcode': '',
            'default_country': ''
                                            })
        self.assertTrue(
            userprofile_form.is_valid())
