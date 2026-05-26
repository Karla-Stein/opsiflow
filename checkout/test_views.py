from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from unittest.mock import patch
from django.core.files.uploadedfile import SimpleUploadedFile

from products.models import Product, ProductOption
from checkout.models import Order, OrderLineItem


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


class TestCheckoutView(TestCase):
    """
    Tests for the checkout view.
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

        self.profile = self.user.userprofile
        self.profile.default_first_name = 'Alice'
        self.profile.default_last_name = 'Lastname'
        self.profile.default_country = 'GB'
        self.profile.save()

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

    @patch('checkout.views.stripe.PaymentIntent.create')
    def test_order_form_is_prepopulated(self, mock_intent):
        """
        Test that the order form prepopulates with saved user data.
        """
        mock_intent.return_value.client_secret = 'test_secret_123'

        session = self.client.session
        session['bag'] = {str(self.product_option.pk): 1}
        session.save()

        response = self.client.get(
                reverse('checkout')
            )

        form = response.context['order_form']

        self.assertTemplateUsed(response,
                                'checkout/checkout.html')

        self.assertEqual(response.status_code, 200, msg='Status code not 200')
        self.assertEqual(form.initial['user_first_name'],
                         'Alice')
        self.assertEqual(form.initial['user_last_name'],
                         'Lastname')
        self.assertEqual(form.initial['billing_country'],
                         'GB')

        mock_intent.assert_called_once()

    @patch('checkout.views.stripe.PaymentIntent.create')
    def test_payment_intent_uses_correct_amount(self, mock_intent):
        """
        Test that Stripe payment Itent is created with the correct amount.
        """
        mock_intent.return_value.client_secret = 'test_secret_123'

        session = self.client.session
        session['bag'] = {str(self.product_option.pk): 1}
        session.save()

        response = self.client.get(reverse('checkout'))
        expected_price = int(self.product_option.unit_price) * 100

        self.assertEqual(response.status_code, 200, msg="Status code not 200")
        mock_intent.assert_called_once_with(
            amount=expected_price,
            currency='gbp')

    def test_login_required(self):
        """
        Test that login is required and redirect leads to
        login page.
        """
        self.client.logout()

        response = self.client.get(
                reverse('checkout')
            )

        self.assertRedirects(
            response,
            '/accounts/login/?next=/checkout/'
        )


class TestCheckoutSuccessView(TestCase):
    """
    Tests for the checkout success view.
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

        self.order = Order(
            order_number='12345',
            payment_id='6758594',
        )
        self.order.save()

        session = self.client.session
        session['bag'] = {str(self.product_option.pk): 1}
        session['form_data'] = {
            'user_first_name': 'Alice',
            'user_last_name': 'Lastname',
            'user_email': 'alice@lastname.com',
            'billing_address_1': 'Test Drive',
            'billing_city': 'London',
            'billing_country': 'GB',
            'save_details': True,
            'status': 1,
        }
        session.save()

    @patch('checkout.views.stripe.PaymentIntent.retrieve')
    def test_checkout_success_page_renders_correctly(self, mock_retrieve):
        """
        Test that checkout success page renders successfully.
        """
        mock_retrieve.return_value.status = 'succeeded'

        response = self.client.get(
            reverse('checkout_success') + '?payment_intent=6758594')

        self.assertTemplateUsed(response,
                                'checkout/checkout_success.html')

        self.assertEqual(response.status_code, 200, msg='Status code not 200')

    @patch('checkout.views.stripe.PaymentIntent.retrieve')
    def test_order_is_created_after_successfull_payment(self, mock_retrieve):
        """
        Test that the view creates the order after successfull payment intent.
        """
        self.order.delete()

        mock_retrieve.return_value.status = 'succeeded'

        response = self.client.get(
            reverse('checkout_success') + '?payment_intent=6758594')

        order_exists = Order.objects.filter(payment_id=6758594).exists()

        self.assertEqual(response.status_code, 200, msg='Status code not 200')
        self.assertTrue(order_exists)

    @patch('checkout.views.EmailMultiAlternatives.send')
    @patch('checkout.views.stripe.PaymentIntent.retrieve')
    def test_session_cleared_after_after_successful_save(self,
                                                         mock_retrieve,
                                                         mock_send):
        """
        Test that the session bag and form data is cleared after email is sent.
        """
        mock_retrieve.return_value.status = 'succeeded'
        mock_send.return_value.send = True

        response = self.client.get(
            reverse('checkout_success') + '?payment_intent=6758594')

        session = self.client.session

        self.assertEqual(response.status_code, 200, msg='Status code not 200')
        self.assertNotIn('bag', session)
        self.assertNotIn('checkout_data', session)

    def test_login_required(self):
        """
        Test that login is required and redirect leads to
        login page.
        """
        self.client.logout()

        response = self.client.get(
                reverse('checkout_success')
            )

        self.assertRedirects(
            response,
            '/accounts/login/?next=/checkout/success/'
        )


class TestDownloadView(TestCase):
    """
    Tests for the download view.
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

        self.profile = self.user.userprofile

        self.product = Product(
            name='Test Automation',
            description='Test description',
            excerpt='Test excerpt',
        )
        self.product.save()

        self.product_option = ProductOption(
            product=self.product,
            name='DIY Template',
            unit_price=99.00,
            fulfilment_choice=0,
            download_file=SimpleUploadedFile('file.txt', b"file_content",
                                             content_type='json')
        )
        self.product_option.save()

        self.order = Order(
            user_profile=self.profile,
            order_number='12345',
            payment_id='6758594',
        )
        self.order.save()

        self.lineitem = OrderLineItem(
            item_option=self.product_option,
            order=self.order
        )
        self.lineitem.save()

    def test_purchaser_can_dowload_file(self):
        """
        Test that only the owner of the file can ndownload the purchased file.
        """

        response = self.client.get(reverse('download',
                                           args=[self.lineitem.pk]))

        self.assertEqual(response.status_code, 200, msg='Status code not 200')

    def test_download_prohibited_for_non_owner(self):
        """
        Test that non owner are rejected from downloading.
        """
        self.client.logout()

        self.user = User.objects.create_user(
            username='New_Test_user',
            password='New_testpw123',
            email='New_test@test.com'
        )

        self.client.login(
            username='New_Test_user',
            password='New_testpw123'
        )

        response = self.client.get(reverse('download',
                                           args=[self.lineitem.pk]))

        self.assertEqual(
            response.status_code,
            403,
            msg='Status code not 403, download allowed')

    def test_max_three_downloads_allowed(self):
        """
        Test that user is redirected to homepage after
        attemting to download a fourth time.
        """
        self.client.get(reverse('download',
                                args=[self.lineitem.pk]))
        self.client.get(reverse('download',
                                args=[self.lineitem.pk]))
        self.client.get(reverse('download',
                                args=[self.lineitem.pk]))
        response = self.client.get(reverse('download',
                                           args=[self.lineitem.pk]))

        self.assertEqual(response.status_code, 302, msg='Status code not 302')
        self.assertRedirects(
            response,
            '/'
        )
