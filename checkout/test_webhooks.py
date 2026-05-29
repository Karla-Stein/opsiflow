from django.test import RequestFactory, TestCase
from django.contrib.auth.models import User
from unittest.mock import patch, MagicMock

from products.models import Product, ProductOption
from .webhook_handler import StripeWebhookHandler
from checkout.models import Order

import json


class TestStripeWebhookHandler(TestCase):

    """
    Tests for the Stripe webhook handler.
    """

    def setUp(self):
        self.factory = RequestFactory()
        self.request = self.factory.post('/checkout/wh/')
        self.user = User.objects.create_user(
            username='Test_user',
            password='testpw123',
            email='test@test.com'
        )

        self.profile = self.user.userprofile

        self.product = Product.objects.create(
            name='Test Automation',
            description='Test description',
            excerpt='Test excerpt',
        )

        self.product_option = ProductOption.objects.create(
            product=self.product,
            name='Setup Service',
            unit_price=99.00,
            fulfilment_choice=1,
        )

        self.handler = StripeWebhookHandler(self.request)

    @patch('checkout.webhook_handler.stripe.Charge.retrieve')
    def test_webhook_creates_order_if_checkout_success_did_not(self,
                                                               mock_charge):
        """
        Test that the webhook creates an order if checkout success did not.
        """
        mock_charge.return_value.amount = 9900
        mock_charge.return_value.billing_details.name = 'Alice Lastname'
        mock_charge.return_value.billing_details.email = 'alice@lastname.com'
        mock_charge.return_value.billing_details.phone = '12345'
        mock_charge.return_value.billing_details.address.line1 = 'Test Drive'
        mock_charge.return_value.billing_details.address.line2 = ''
        mock_charge.return_value.billing_details.address.city = 'London'
        mock_charge.return_value.billing_details.address.postal_code = ''
        mock_charge.return_value.billing_details.address.state = ''
        mock_charge.return_value.billing_details.address.country = 'GB'

        event = MagicMock()
        event.__getitem__.return_value = 'payment_intent.succeeded'

        event.data.object.id = '6758594'
        event.data.object.amount = 9900
        event.data.object.metadata.bag = json.dumps(
            {str(self.product_option.pk): 1})
        event.data.object.metadata.user_profile = self.profile.pk
        event.data.object.metadata.save_details = True

        order_created_by_success_view = Order.objects.filter(
            payment_id='6758594').exists()
        self.assertFalse(order_created_by_success_view)

        response = self.handler.handle_payment_intent_succeeded(event)

        order_created_by_webhook = Order.objects.filter(
            payment_id='6758594').exists()

        self.assertEqual(response.status_code, 200)
        self.assertTrue(order_created_by_webhook)
