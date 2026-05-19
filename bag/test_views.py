from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from products.models import Product, ProductOption


class TestBagView(TestCase):
    """
    Test for the view bag view.
    """
    def setUp(self):
        self.user = User.objects.create_user(
            username='Test_user',
            password='testpw123'
        )

        self.client.login(
            username='Test_user',
            password='testpw123'
        )

    def test_view_bag_renders_correctly(self):
        """
        Test that response code returns 200 and the correct template is used.
        """
        response = self.client.get(reverse(
            'bag'))

        self.assertEqual(response.status_code, 200, msg="Status code not 200")
        self.assertTemplateUsed(response,
                                'bag/bag.html')

    def test_login_required(self):
        """
        Test that login is required and redirect leads to
        login to view bag page.
        """
        self.client.logout()

        response = self.client.get(
                reverse('bag')
            )

        self.assertRedirects(
            response,
            '/accounts/login/?next=/bag/'
        )


class TestAddToBagView(TestCase):
    """
    Tests for the add to bag view.
    """
    def setUp(self):
        self.user = User.objects.create_user(
            username='Test_user',
            password='testpw123'
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

    def test_add_to_bag_adds_product_to_session(self):
        """
        Test that the add to bag view adds product options to the bag session.
        """
        response = self.client.post(
            reverse('add_to_bag'), {
                'selected_option_pk': self.product_option.pk,
                'redirect_url': reverse('products')
                 }
            )

        session = self.client.session
        bag = session.get('bag')

        # redirects always return status code 302
        self.assertEqual(response.status_code, 302, msg="Status code not 302")
        self.assertIn(str(self.product_option.pk), bag)

    def test_login_required_to_add_to_bag(self):
        """
        Test that login is required and user redirected to login. .
        """
        self.client.logout()

        response = self.client.get(
                reverse('add_to_bag')
            )
        self.assertEqual(response.status_code, 302, msg="Status code not 302")
        self.assertRedirects(
            response,
            '/accounts/login/?next=/bag/add-to-bag/'
        )
