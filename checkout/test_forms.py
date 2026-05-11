from django.test import TestCase
from .forms import OrderForm


class TestOrderForm(TestCase):

    def test_all_required_fields_are_valid(self):
        """Positive test for all required fields"""
        order_form = OrderForm({
            'user_first_name': 'test',
            'user_last_name': 'test',
            'user_email': 'email@address.com',
            'user_phone': '',
            'billing_address_1': 'test drive',
            'billing_address_2': '',
            'billing_county': '',
            'billing_city': 'test',
            'billing_postalcode': '',
            'billing_country': 'GB'
            })
        self.assertTrue(
            order_form.is_valid(),
            msg='Form is missing required fields or required '
            'input has the wrong format')

    def test_email_field_is_invalid(self):
        """Negative test for email fields"""
        order_form = OrderForm({
            'user_first_name': 'test',
            'user_last_name': 'test',
            'user_email': 'emailaddress.com',
            'user_phone': '',
            'billing_address_1': 'test drive',
            'billing_address_2': '',
            'billing_county': '',
            'billing_city': 'test',
            'billing_postalcode': '',
            'billing_country': 'GB'
            })
        self.assertFalse(
            order_form.is_valid(),
            msg='Email format is correct')

    def test_first_name_field_is_invalid(self):
        """Negative test for first name fields"""
        order_form = OrderForm({
            'user_first_name': '',
            'user_last_name': 'test',
            'user_email': 'email@address.com',
            'user_phone': '',
            'billing_address_1': 'test drive',
            'billing_address_2': '',
            'billing_county': '',
            'billing_city': 'test',
            'billing_postalcode': '',
            'billing_country': 'GB'
            })
        self.assertFalse(
            order_form.is_valid(),
            msg='First name is provided')

    def test_name_field_is_invalid(self):
        """Negative test for name fields"""
        order_form = OrderForm({
            'user_first_name': 'test',
            'user_last_name': '',
            'user_email': 'email@address.com',
            'user_phone': '',
            'billing_address_1': 'test drive',
            'billing_address_2': '',
            'billing_county': '',
            'billing_city': 'test',
            'billing_postalcode': '',
            'billing_country': 'GB'
            })
        self.assertFalse(
            order_form.is_valid(),
            msg='Name is provided')

    def test_email_field_not_provided(self):
        """Negative test for omitted email field"""
        order_form = OrderForm({
            'user_first_name': 'test',
            'user_last_name': 'test',
            'user_email': '',
            'user_phone': '',
            'billing_address_1': 'test drive',
            'billing_address_2': '',
            'billing_county': '',
            'billing_city': 'test',
            'billing_postalcode': '',
            'billing_country': 'GB'
            })
        self.assertFalse(
            order_form.is_valid(),
            msg='Email is provided')

    def test_billing_1_not_provided(self):
        """Negative test for omitted billing_1 field"""
        order_form = OrderForm({
            'user_first_name': 'test',
            'user_last_name': 'test',
            'user_email': 'email@address.com',
            'user_phone': '',
            'billing_address_1': '',
            'billing_address_2': '',
            'billing_county': '',
            'billing_city': 'test',
            'billing_postalcode': '',
            'billing_country': 'GB'
            })
        self.assertFalse(
            order_form.is_valid(),
            msg='Billing 1 is provided')

    def test_city_not_provided(self):
        """Negative test for omitted city field"""
        order_form = OrderForm({
            'user_first_name': 'test',
            'user_last_name': 'test',
            'user_email': 'email@address.com',
            'user_phone': '',
            'billing_address_1': 'test drive',
            'billing_address_2': '',
            'billing_county': '',
            'billing_city': '',
            'billing_postalcode': '',
            'billing_country': 'GB'
            })
        self.assertFalse(
            order_form.is_valid(),
            msg='City is provided')

    def test_country_not_provided(self):
        """Negative test for omitted country field"""
        order_form = OrderForm({
            'user_first_name': 'test',
            'user_last_name': 'test',
            'user_email': 'email@address.com',
            'user_phone': '',
            'billing_address_1': 'test drive',
            'billing_address_2': '',
            'billing_county': '',
            'billing_city': 'test',
            'billing_postalcode': '',
            'billing_country': ''
            })
        self.assertFalse(
            order_form.is_valid(),
            msg='Country is provided')
