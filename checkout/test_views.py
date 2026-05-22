from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from unittest.mock import patch

from products.models import Product, ProductOption


class TestCacheCheckoutDataView(TestCase):
    """
    Tests for the cache checkout data view.
    """
    def setUp(self):
        self.user = User.objects.create_user(
            username='Test_user',
            password='testpw123',
            email='test@test.com'
        )

        self.client.login(
            username='Test_user',
            password='testpw123'
        )

        self.product = Product(
            name='Test Automation',
            description='Test description',
            excerpt='Test excerpt',
        )
        self.product.save()

        self.product_option = ProductOption(
            product=self.product,
            name='Setup Service',
            unit_price=99.00,
            fulfilment_choice=1,
        )
        self.product_option.save()

    @patch('checkout.views.stripe.PaymentIntent.modify')
    def test_cache_checkout_data_saves_form_data_and_updates_stripe(
            self,
            mock_modify):
        """
        Test that checkout form data is saved in the session
        and Stripe metadata is updated.
        """
        session = self.client.session
        session['bag'] = {str(self.product_option): 1}
        session.save()
        response = self.client.post(
            reverse('cache_checkout_data'),
            {
                'user_first_name': 'Alice',
                'user_last_name': 'Lastname',
                'user_email': 'alice@lastname.com',
                'user_phone': '',
                'billing_address_1': 'Test Drive',
                'billing_address_2': '',
                'billing_county': '',
                'billing_city': 'London',
                'billing_postalcode': '',
                'billing_country': 'GB',
                'save_details': 'on',
                'client_secret': 'test_secret_123',
            }
        )

        session = self.client.session
        self.assertEqual(response.status_code, 200, msg="Status code not 200")
        self.assertJSONEqual(response.content, {'success': True})
        self.assertEqual(
            session['form_data']['user_first_name'],
            'Alice'
        )

        mock_modify.assert_called_once()

    def test_login_required(self):
        """
        Test that login is required and redirect leads to
        login page.
        """
        self.client.logout()

        response = self.client.get(
                reverse('cache_checkout_data')
            )

        self.assertRedirects(
            response,
            '/accounts/login/?next=/checkout/cache_checkout_data/'
        )
