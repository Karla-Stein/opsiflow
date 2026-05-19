from django.test import TestCase
from django.urls import reverse


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
