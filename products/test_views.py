from django.test import TestCase
from django.urls import reverse

from .models import Category, Product, ProductOption


class TestAllProductsView(TestCase):
    """Tests for all_products view"""

    def setUp(self):
        self.category = Category(
            name="Category name"
        )
        self.category.save()

        self.product_1 = Product(
            category=self.category,
            name="High-Intent Lead Magnet Delivery System 1",
            description="test description 1",
            excerpt="Product excerpt 1",
            image_url="",
            image="")
        self.product_1.save()

        self.product_option_1 = ProductOption(
            product=self.product_1,
            name="test product option 1",
            description="test description product option 1",
            unit_price=100.00,
            fulfilment_choice=1,
            download_file=None,
            tier=None,
            delivery_days=2)
        self.product_option_1.save()

        self.product_2 = Product(
            category=self.category,
            name="test Product 2",
            description="test description 2",
            excerpt="Product excerpt 2",
            image_url="",
            image="")
        self.product_2.save()

        self.product_option_2 = ProductOption(
            product=self.product_2,
            name="test product option 2",
            description="test description product option 2",
            unit_price=50.00,
            fulfilment_choice=0,
            download_file="",
            tier=None,
            delivery_days=None)
        self.product_option_2.save()

        self.product_3 = Product(
            category=self.category,
            name="Booking test 3",
            description="test description 3",
            excerpt="Product excerpt 3",
            image_url="",
            image="")
        self.product_3.save()

        self.product_option_3 = ProductOption(
            product=self.product_3,
            name="test product option 3",
            description="test description product option 3",
            unit_price=99.00,
            fulfilment_choice=1,
            download_file=None,
            tier=None,
            delivery_days=3)
        self.product_option_3.save()

    def test_products_page_renders(self):
        """
        Test that page returns status code 200, name and excerpt are
        displayed and correct template is used.
        """
        response = self.client.get(reverse(
            'products'))

        self.assertEqual(response.status_code, 200, msg="Status code not 200")
        self.assertIn(b"High-Intent Lead Magnet Delivery System 1",
                      response.content,
                      msg="Product name is not displayed")
        self.assertIn(b"Product excerpt 2",
                      response.content,
                      msg="Product excerpt is not displayed")
        self.assertTemplateUsed(response,
                                'products/products.html')

    def test_sort_by_name_ascending(self):
        """
        Test that name sorts by ascending order.
        """
        response = self.client.get(reverse('products'),
                                   {'sort': 'name', 'direction': 'asc'})
        self.assertEqual(response.status_code, 200)
        products = response.context['products']
        names = [product.name for product in products]
        self.assertEqual(
            names,
            ['Booking test 3', 'High-Intent Lead Magnet Delivery System 1',
             'test Product 2']
                        )

    def test_sort_by_name_descending(self):
        """
        Test that name sorts by descending order.
        """
        response = self.client.get(reverse('products'),
                                   {'sort': 'name', 'direction': 'desc'})
        self.assertEqual(response.status_code, 200)
        products = response.context['products']
        names = [product.name for product in products]
        self.assertEqual(
            names,
            ['test Product 2',
             'High-Intent Lead Magnet Delivery System 1',
             'Booking test 3']
                        )

    def test_sort_by_complexity_ascending(self):
        """
        Test that complexity sorts by ascending order.
        """
        response = self.client.get(
            reverse('products'),
            {'sort': 'complexity', 'direction': 'asc'})
        products = response.context['products']
        names = [product.name for product in products]
        self.assertEqual(
            names,
            ['test Product 2',
             'High-Intent Lead Magnet Delivery System 1',
             'Booking test 3']
                        )

    def test_sort_by_complexity_descending(self):
        """
        Test that complexity sorts by descending order.
        """
        response = self.client.get(
            reverse('products'),
            {'sort': 'complexity', 'direction': 'desc'})
        products = response.context['products']
        names = [product.name for product in products]
        self.assertEqual(
            names,
            ['Booking test 3',
             'High-Intent Lead Magnet Delivery System 1',
             'test Product 2',]
                        )

    def test_sort_by_price_ascending(self):
        """
        Test that price sorts by ascending order.
        """
        response = self.client.get(
            reverse('products'),
            {'sort': 'price', 'direction': 'asc'})
        products = response.context['products']
        names = [product.name for product in products]
        self.assertEqual(
            names,
            ['test Product 2',
             'Booking test 3',
             'High-Intent Lead Magnet Delivery System 1',
             ]
                        )

    def test_sort_by_price_descending(self):
        """
        Test that price sorts by descending order.
        """
        response = self.client.get(
            reverse('products'),
            {'sort': 'price', 'direction': 'desc'})
        products = response.context['products']
        names = [product.name for product in products]
        self.assertEqual(
            names,
            ['High-Intent Lead Magnet Delivery System 1',
             'Booking test 3',
             'test Product 2',
             ]
                        )


class TestProductDetailView(TestCase):
    """
    Tests for product_detail view.
    """

    def setUp(self):
        self.category = Category(
            name="Category name"
        )
        self.category.save()

        self.product_1 = Product(
            category=self.category,
            name="High-Intent Lead Magnet Delivery System 1",
            description="test description 1",
            excerpt="Product excerpt 1",
            image_url="",
            image="")
        self.product_1.save()

        self.product_option_1 = ProductOption(
            product=self.product_1,
            name="test product option 1",
            description="test description product option 1",
            unit_price=100.00,
            fulfilment_choice=1,
            download_file=None,
            tier=None,
            delivery_days=2)
        self.product_option_1.save()

    def test_product_detail_page_renders(self):
        """
        Test that response code is 200, correct template is used
        and correct product was passed to the context.
        """
        response = self.client.get(reverse(
            'product_detail',  args=[self.product_1.pk]))

        self.assertEqual(response.status_code, 200, msg="Status code not 200")
        self.assertTemplateUsed(response,
                                'products/product_detail.html')
        self.assertEqual(str(response.context['product']),
                         "High-Intent Lead Magnet Delivery System 1")
