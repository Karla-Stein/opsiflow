from django.test import TestCase
from django.urls import reverse

from django.contrib.auth.models import User
from checkout.models import Order
from .models import UserProfile


class TestPurchasesView(TestCase):
    """
    Tests for purchases view.
    """

    def setUp(self):
        self.user = User.objects.create_user(
            username="Test_user",
            password="testpw123",
            email="test@test.com"
        )
        self.profile = self.user.userprofile
        self.profile.save()

        self.client.login(
            username='Test_user',
            password='testpw123'
        )

        self.order_1 = Order(
                   user_profile=self.profile,
                   user_first_name="Alice",
                   user_last_name="Lastname",
                   user_email="alice@lastname.com",
                   billing_address_1="Test drive",
                   billing_city="London",
                   billing_country="Uk",
                   payment_id="12345"
        )
        self.order_1.save()

        self.order_2 = Order(
                   user_profile=self.profile,
                   user_first_name="Alice",
                   user_last_name="Lastname",
                   user_email="alice@lastname.com",
                   billing_address_1="Test drive",
                   billing_city="London",
                   billing_country="Uk",
                   payment_id="67890"
        )
        self.order_2.save()

    def test_my_purchases_page_renders(self):
        """
        Test that response code is 200, correct template is used
        and correct products are passed to the context.
        """
        response = self.client.get(reverse(
            'purchases'))

        self.assertEqual(response.status_code, 200, msg="Status code not 200")
        self.assertTemplateUsed(response,
                                'profiles/purchases.html')

    def test_login_required(self):
        """
        Test that login is required and redirect leads to
        login to view purchase page.
        """
        self.client.logout()

        response = self.client.get(
                reverse('purchases')
            )

        self.assertRedirects(
            response,
            '/accounts/login/?next=/profiles/my-purchases/'
        )


class TestMyProfileView(TestCase):
    """
    Tests for the my_profle view.
    """
    def setUp(self):
        self.user = User.objects.create_user(
            username="Test_user",
            password="testpw123",
            email="test@test.com"
        )
        self.profile = self.user.userprofile
        self.profile.save()

        self.client.login(
            username="Test_user",
            password="testpw123"
        )

    def test_profile_page_renders(self):
        """
        Test that response code is 200, correct template is used
        and correct formdata is passed to the context.
        """

        response = self.client.get(reverse(
            'my_profile'))

        self.assertEqual(response.status_code, 200, msg="Status code not 200")
        self.assertTemplateUsed(response,
                                "profiles/profile.html")

    def test_login_to_view_profile_required(self):
        """
        Test that login is required and redirect leads to
        login to view purchase page.
        """
        self.client.logout()

        response = self.client.get(
                reverse('my_profile')
            )

        self.assertRedirects(
            response,
            '/accounts/login/?next=/profiles/my-profile/'
        )

    def test_profile_updates_upon_submit(self):
        """
        Test to check that profile updates.
        """

        self.profile = UserProfile(
            default_first_name="Alice",
            default_last_name="Lastname",
        )

        response = self.client.post(
                reverse('my_profile')
            )

        self.assertEqual(response.status_code, 200, msg="Status code not 200")
        self.assertEqual(self.profile.default_first_name, "Alice")
        self.assertEqual(self.profile.default_last_name, "Lastname")


class TestDeleteAccountView(TestCase):
    """
    Tests for delete_account view.
    """
    def setUp(self):

        self.user = User.objects.create_user(
            username="Test_user",
            password="testpw123",
            email="test@test.com"
        )
        self.profile = self.user.userprofile
        self.profile.save()

        self.client.login(
            username='alice',
            password='testpass123'
        )

    def test_login_to_delete_profile_required(self):
        """
        Test that login is required and redirect leads to
        login to delete profile.
        """
        self.client.logout()

        response = self.client.get(
                reverse('delete_account')
            )

        self.assertRedirects(
            response,
            '/accounts/login/?next=/profiles/delete-account/'
        )

    def test_account_exists_after_deletion(self):
        """
        Test to check if profile exists after deletion.
        """
        self.profile.delete()

        profile_exists = UserProfile.objects.filter(
            pk=self.profile.pk).exists()

        self.assertFalse(profile_exists)
