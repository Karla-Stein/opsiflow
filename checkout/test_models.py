from django.test import TestCase
from django.contrib.auth.models import User

from profiles.models import UserProfile
from .models import Order, OrderLineItem
from products.models import Product, ProductOption


class OrderModelTest(TestCase):
    """
    Tests for the Category model.
    """

    def test_order_number_is_created(self):
        """
        Test that _generate_order_number creates an order number."
        """
        user = User.objects.create_user(
            username='alice',
            password='testpass123'
            )

        profile = UserProfile.objects.get(user=user)

        order = Order.objects.create(
            order_number="",
            user_profile=profile,
            user_first_name="alice",
            user_last_name="lastname",
            user_email="alice@wonderland.com",
            user_phone="12345",
            billing_address_1="Test Drive",
            billing_address_2="",
            billing_county="",
            billing_city="London",
            billing_postalcode="E99999",
            billing_country="UK",
            order_total=100.00,
            payment_id="",
            status=0,
            created_at="30/08/1961",
            )

        result = order._generate_order_number()

        self.assertIsNotNone(result,
                             msg='No order number was created')

    def test_order_str_returns_correct_str(self):
        """
        Test that __str__ returns "Order number:
        {self.order_number}. Status: {self.status}.""
        """
        user = User.objects.create_user(
            username='alice',
            password='testpass123'
            )

        profile = UserProfile.objects.get(user=user)

        order = Order.objects.create(
            order_number="DC0E141466",
            user_profile=profile,
            user_first_name="alice",
            user_last_name="lastname",
            user_email="alice@wonderland.com",
            user_phone="12345",
            billing_address_1="Test Drive",
            billing_address_2="",
            billing_county="",
            billing_city="London",
            billing_postalcode="E99999",
            billing_country="UK",
            order_total=100.00,
            payment_id="",
            status=2,
            created_at="30/08/1961",
            )

        result = str(order)

        self.assertEqual(
            result,
            "Order number: DC0E141466. Status: 2",
            msg='String not or wrong returned')

    def test_save_overrides_original_save_method_to_set_orderNumber(self):
        """
        Test to override the original save method to set the order number
        if it hasn't been set already""
        """
        user = User.objects.create_user(
            username='alice',
            password='testpass123'
            )

        profile = UserProfile.objects.get(user=user)

        order = Order.objects.create(
            order_number=None,
            user_profile=profile,
            user_first_name="alice",
            user_last_name="lastname",
            user_email="alice@wonderland.com",
            user_phone="12345",
            billing_address_1="Test Drive",
            billing_address_2="",
            billing_county="",
            billing_city="London",
            billing_postalcode="E99999",
            billing_country="UK",
            order_total="100.00",
            payment_id="",
            status=2,
            created_at="30/08/1961",
            )

        result = order.order_number

        self.assertIsNotNone(
            result,
            msg="Ordernumber does not exist")

    def test_update_total_updates_dynamically(self):
        """
        Test to check that update_total retrives the sum of all line_items""
        """
        user = User.objects.create_user(
            username='alice',
            password='testpass123'
            )

        profile = UserProfile.objects.get(user=user)

        order = Order.objects.create(
            order_number="",
            user_profile=profile,
            user_first_name="alice",
            user_last_name="lastname",
            user_email="alice@wonderland.com",
            user_phone="12345",
            billing_address_1="Test Drive",
            billing_address_2="",
            billing_county="",
            billing_city="London",
            billing_postalcode="E99999",
            billing_country="UK",
            order_total=0,
            payment_id="",
            status=2,
            created_at="30/08/1961",
            )

        product_1 = Product.objects.create(
            name='Lead-to-Invoice Automation',
            description='Capture leads and send invoices',
            excerpt='',
            image_url='',
            image='',
            )

        product_2 = Product.objects.create(
            name='Email Automation',
            description='Capture leads and send invoices',
            excerpt='',
            image_url='',
            image='',
            )

        product_option_1 = ProductOption.objects.create(
            product=product_1,
            name="option name",
            description="description",
            unit_price=99.00,
            fulfilment_choice=0,
            download_file="",
            tier=None,
            delivery_days=0,
        )

        product_option_2 = ProductOption.objects.create(
            product=product_2,
            name="option name",
            description="description",
            unit_price=50.00,
            fulfilment_choice=0,
            download_file="",
            tier=0,
            delivery_days=0,
        )

        OrderLineItem.objects.create(
            item_option=product_option_1,
            order=order,
            quantity=1,
            lineitem_total=product_option_1.unit_price,
            download_count=3,
        )

        OrderLineItem.objects.create(
            item_option=product_option_2,
            order=order,
            quantity=1,
            lineitem_total=product_option_2.unit_price,
            download_count=3,
        )

        order.update_total()
        result = order.order_total

        self.assertEqual(
            result, 149.00,
            msg="Order_total is not updating accordingly")

    def test_order_still_exists_after_profile_delete(self):
        """
        Test to check that the order is not deleted with Profile deletion.""
        """
        user = User.objects.create_user(
            username='alice',
            password='testpass123'
            )

        profile = UserProfile.objects.get(user=user)

        order = Order.objects.create(
            order_number="",
            user_profile=profile,
            user_first_name="alice",
            user_last_name="lastname",
            user_email="alice@wonderland.com",
            user_phone="12345",
            billing_address_1="Test Drive",
            billing_address_2="",
            billing_county="",
            billing_city="London",
            billing_postalcode="E99999",
            billing_country="UK",
            order_total=0,
            payment_id="",
            status=2,
            created_at="30/08/1961",
            )

        profile.delete()
        result = Order.objects.filter(pk=order.pk).exists()

        self.assertTrue(result,
                        msg="Order does not exist")


class OrderLineItemModelTest(TestCase):
    """
    Tests for the OrderLineItem model.
    """

    def test_save_method_updates_lineitem_total(self):
        """
        Test that the save method updates the lineitem_total."
        """
        user = User.objects.create_user(
            username='alice',
            password='testpass123'
            )

        profile = UserProfile.objects.get(user=user)

        order = Order.objects.create(
            order_number="",
            user_profile=profile,
            user_first_name="alice",
            user_last_name="lastname",
            user_email="alice@wonderland.com",
            user_phone="12345",
            billing_address_1="Test Drive",
            billing_address_2="",
            billing_county="",
            billing_city="London",
            billing_postalcode="E99999",
            billing_country="UK",
            order_total=100.00,
            payment_id="",
            status=0,
            created_at="30/08/1961",
            )

        product_1 = Product.objects.create(
            name='Lead-to-Invoice Automation',
            description='Capture leads and send invoices',
            excerpt='',
            image_url='',
            image='',
            )

        product_option_1 = ProductOption.objects.create(
            product=product_1,
            name="option name",
            description="description",
            unit_price=99.00,
            fulfilment_choice=0,
            download_file="",
            tier=None,
            delivery_days=0,
        )

        orderline_item = OrderLineItem.objects.create(
            item_option=product_option_1,
            order=order,
            quantity=1,
            lineitem_total=0,
            download_count=3,
        )

        result = orderline_item.lineitem_total

        self.assertEqual(result, 99.00,
                         msg='Lineitem total is not correct')

    def test_orderlineitem_is_deleted_upon_order_deletion(self):
        """
        Test that the orderlineitem deletes if relational order is deleted."
        """
        user = User.objects.create_user(
            username='alice',
            password='testpass123'
            )

        profile = UserProfile.objects.get(user=user)

        order = Order.objects.create(
            order_number="",
            user_profile=profile,
            user_first_name="alice",
            user_last_name="lastname",
            user_email="alice@wonderland.com",
            user_phone="12345",
            billing_address_1="Test Drive",
            billing_address_2="",
            billing_county="",
            billing_city="London",
            billing_postalcode="E99999",
            billing_country="UK",
            order_total=100.00,
            payment_id="",
            status=0,
            created_at="30/08/1961",
            )

        product_1 = Product.objects.create(
            name='Lead-to-Invoice Automation',
            description='Capture leads and send invoices',
            excerpt='',
            image_url='',
            image='',
            )

        product_option_1 = ProductOption.objects.create(
            product=product_1,
            name="option name",
            description="description",
            unit_price=99.00,
            fulfilment_choice=0,
            download_file="",
            tier=None,
            delivery_days=0,
        )

        orderline_item = OrderLineItem.objects.create(
            item_option=product_option_1,
            order=order,
            quantity=1,
            lineitem_total=0,
            download_count=3,
        )

        order.delete()
        item = OrderLineItem.objects.filter(pk=orderline_item.pk).exists()

        self.assertFalse(item,
                         msg='Lineitem still exists')

    def test_str_representation_returns_depending_order_number(self):
        """
        Test that the str method returns which order
        number the lineitem belongs to."
        """
        user = User.objects.create_user(
            username='alice',
            password='testpass123'
            )

        profile = UserProfile.objects.get(user=user)

        order = Order.objects.create(
            order_number="",
            user_profile=profile,
            user_first_name="alice",
            user_last_name="lastname",
            user_email="alice@wonderland.com",
            user_phone="12345",
            billing_address_1="Test Drive",
            billing_address_2="",
            billing_county="",
            billing_city="London",
            billing_postalcode="E99999",
            billing_country="UK",
            order_total=100.00,
            payment_id="",
            status=0,
            created_at="30/08/1961",
            )

        product_1 = Product.objects.create(
            name='Lead-to-Invoice Automation',
            description='Capture leads and send invoices',
            excerpt='',
            image_url='',
            image='',
            )

        product_option_1 = ProductOption.objects.create(
            product=product_1,
            name="option name",
            description="description",
            unit_price=99.00,
            fulfilment_choice=0,
            download_file="",
            tier=None,
            delivery_days=0,
        )

        orderline_item = OrderLineItem.objects.create(
            item_option=product_option_1,
            order=order,
            quantity=1,
            lineitem_total=0,
            download_count=3,
        )

        result = str(orderline_item)

        self.assertEqual(result, f'OrderLineItem belongs to Order number: {
            orderline_item.order.order_number}.',
            msg='String representation returned incorrectly.')

    def test_download_count_defaults_to_three(self):
        """
        Test that the download count default is three."
        """
        user = User.objects.create_user(
            username='alice',
            password='testpass123'
            )

        profile = UserProfile.objects.get(user=user)

        order = Order.objects.create(
            order_number="",
            user_profile=profile,
            user_first_name="alice",
            user_last_name="lastname",
            user_email="alice@wonderland.com",
            user_phone="12345",
            billing_address_1="Test Drive",
            billing_address_2="",
            billing_county="",
            billing_city="London",
            billing_postalcode="E99999",
            billing_country="UK",
            order_total=100.00,
            payment_id="",
            status=0,
            created_at="30/08/1961",
            )

        product_1 = Product.objects.create(
            name='Lead-to-Invoice Automation',
            description='Capture leads and send invoices',
            excerpt='',
            image_url='',
            image='',
            )

        product_option_1 = ProductOption.objects.create(
            product=product_1,
            name="option name",
            description="description",
            unit_price=99.00,
            fulfilment_choice=0,
            download_file="",
            tier=None,
            delivery_days=0,
        )

        orderline_item = OrderLineItem.objects.create(
            item_option=product_option_1,
            order=order,
            quantity=1,
            lineitem_total=0,
        )

        result = orderline_item.download_count

        self.assertEqual(result, 3,
                         msg='Download count does not default to three.')
