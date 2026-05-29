from django.test import TestCase
from django.core.exceptions import ValidationError
from .models import Category, Product, ProductOption


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


class ProductOptionModelTest(TestCase):
    """
    Tests for the ProductOption model.
    """

    def test_productoption_str_returns_productoption_name(self):
        """
        Test that __str__ returns productoption name.
        """

        product = Product.objects.create(
            name='Lead-to-Invoice Automation',
            description='Capture leads and send invoices',
            excerpt='',
            image_url='',
            image='',
            )

        product_option = ProductOption.objects.create(
            product=product,
            name="option name",
            description="description",
            unit_price="99.00",
            fulfilment_choice="0",
            download_file="",
            tier="0",
            delivery_days="0",
        )

        result = str(product_option)

        self.assertEqual(result, 'option name',
                         msg='String message incorrect')

    def test_diy_template_requires_a_download_file(self):
        """
        Negative test that fulfiment choice DIY Template requires a file.
        """

        product = Product.objects.create(
            name='Lead-to-Invoice Automation',
            description='Capture leads and send invoices',
            excerpt='',
            image_url='',
            image='',
            )

        product_option = ProductOption(
            product=product,
            name="option name",
            description="description",
            unit_price="99.00",
            fulfilment_choice=0,
            download_file=None,
            tier=None,
            delivery_days=None,
            )

        with self.assertRaises(ValidationError):
            product_option.full_clean()

    def test_setup_prohibits_a_download_file(self):
        """
        Negative test. Test that fulfiment choice Set Up
        service does not allow file upload.
        """

        product = Product.objects.create(
            name='Lead-to-Invoice Automation',
            description='Capture leads and send invoices',
            excerpt='',
            image_url='',
            image='',
            )

        product_option = ProductOption(
            product=product,
            name="option name",
            description="description",
            unit_price="99.00",
            fulfilment_choice=1,
            download_file=True,
            tier=None,
            delivery_days=None,
            )

        with self.assertRaises(ValidationError):
            product_option.full_clean()

    def test_setup_requires_delivery_days(self):
        """
        Negative test. Test that fulfiment choice Set Up
        service requires delivery days.
        """

        product = Product.objects.create(
            name='Lead-to-Invoice Automation',
            description='Capture leads and send invoices',
            excerpt='',
            image_url='',
            image='',
            )

        product_option = ProductOption(
            product=product,
            name="option name",
            description="description",
            unit_price="99.00",
            fulfilment_choice=1,
            download_file=None,
            tier=None,
            delivery_days=None,
            )

        with self.assertRaises(ValidationError):
            product_option.full_clean()

    def test_fulfilment_choice_and_tier_cannot_coexist(self):
        """
        Negative test. Test that fulfiment choice and tier for custom workflows
        can not coexist.
        """

        product = Product.objects.create(
            name='Lead-to-Invoice Automation',
            description='Capture leads and send invoices',
            excerpt='',
            image_url='',
            image='',
            )

        product_option = ProductOption(
            product=product,
            name="option name",
            description="description",
            unit_price="99.00",
            fulfilment_choice=1,
            download_file=None,
            tier="2",
            delivery_days="2",
            )

        with self.assertRaises(ValidationError):
            product_option.full_clean()
