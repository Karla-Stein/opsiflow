from django.test import TestCase
from django.urls import reverse
from unittest.mock import patch


class TestIndex(TestCase):
    """
    Test for the index view.
    """
    def test_index_renders_the_homepage(self):

        response = self.client.get(reverse(
            'home'))

        self.assertEqual(response.status_code, 200, msg="Status code not 200")
        self.assertTemplateUsed(response,
                                'home/index.html')


class TestContactUs(TestCase):
    """
    Tests for the contact view.
    """
    def test_contact_us_view_renders_the_contact_page(self):
        """
        Test that the contact page is rendered.
        """

        response = self.client.get(reverse(
            'contact'))

        self.assertEqual(response.status_code, 200, msg="Status code not 200")
        self.assertTemplateUsed(response,
                                'home/contact.html')

    @patch('home.views.resend.Emails.send')
    def test_contact_us_view_sends_email_to_owner(self, mock_send):
        """
        Test that the user recievs the feedback message
        after the email was sent.
        """

        # once the form has been validated then the form data are
        # stored in cleaned_data in a key-value pair
        cleaned_data = {
            'name': 'Alice',
            'email': 'alice@email.com',
            'subject': 'Test Subject',
            'message': 'This is a test message'
        }

        response = self.client.post(reverse(
            'contact'), data=cleaned_data)

        mock_send.assert_called_once()

        self.assertEqual(response.status_code, 302,
                         msg='Status code is not 302')

        # mock_send.call_args stores the arguments that where
        # passed to resend.Emails.send().
        # call_args[0] returns the tuple of positional arguments.
        # call_args[0][0] returns the first positional argument, which is
        # the email payload dictionary sent to Resend.
        sent_email = mock_send.call_args[0][0]

        self.assertIn("karlasteinbrink@gmail.com", sent_email["to"])
        self.assertEqual(sent_email["subject"], "Hello World")
        self.assertIn("Alice", sent_email["html"])
        self.assertIn("alice@email.com", sent_email["html"])
        self.assertIn("This is a test message", sent_email["html"])
