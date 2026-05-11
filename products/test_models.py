from django.test import TestCase
from .models import Category, Product


class CategoryModelTest(TestCase):
    """
    Tests for the Category model.
    """

    def test_category_str_returns_category_name(self):
        """
        Test that __str__ returns category name.
        """
        category = Category.objects.create(
            name='lead_generation',
            friendly_name='Lead Generation'
            )

        result = str(category)

        self.assertEqual(result, 'lead_generation',
                         msg='String message incorrect')

    def test_get_friendly_name_returns_friendly_name(self):
        """
        Test that get_friendly_name method returns friendly name.
        """
        category = Category.objects.create(
            name='lead_generation',
            friendly_name='Lead Generation'
            )

        result = category.get_friendly_name()

        self.assertEqual(result, 'Lead Generation',
                         msg='Does not return the friendly name')


class ProductModelTest(TestCase):
    """
    Tests for the Category model.
    """

    def test_product_str_method_returns_product_name(self):
        """
        Test that __str__ returns product name.
        """
        category = Category.objects.create(
            name='lead_generation',
            friendly_name='Lead Generation'
            )
        product = Product.objects.create(
            category=category,
            name='Lead-to-Invoice Automation',
            description='Capture leads and send invoices',
            excerpt='',
            image_url='',
            image='',
            )

        result = str(product)

        self.assertEqual(result, 'Lead-to-Invoice Automation',
                         msg='String message incorrect')

    def test_product_can_be_created_without_category(self):
        """
        Test that a product can be created without depending on a Category.
        """

        product = Product.objects.create(
            name='Lead-to-Invoice Automation',
            description='Capture leads and send invoices',
            excerpt='',
            image_url='',
            image='',
            )

        self.assertIsNone(product.category,
                          msg='Category should be optional')
