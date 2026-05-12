from django.test import TestCase
from django.contrib.auth.models import User
from .models import UserProfile


class UserProfileModelTest(TestCase):
    """
    Tests for the Profile model.
    """
    def test_signal_creates_profile(self):
        """
        Test that signal creates profile on sign up.
        """

        user = User.objects.create_user(
            username='alice',
            password='testpass123'
            )

        profile = UserProfile.objects.filter(user=user).exists()

        self.assertTrue(profile)

    def test_profile_str_returns_profile_of_username(self):
        """
        Test that __str__ returns username.
        """
        user = User.objects.create_user(
            username='alice',
            password='testpass123'
            )

        profile = UserProfile.objects.get(user=user)
        result = str(profile)

        self.assertEqual(result, 'alice')
