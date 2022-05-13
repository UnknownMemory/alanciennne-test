from django.test import TestCase

from ..models import Cart, Item
from product.models import Product


class CartTest(TestCase):
    def setUp(self):
        Cart.objects.create()

    def test_cart(self):
        cart = Cart.objects.get(id=1)
        self.assertEqual(cart.checked_out, False)


class ItemTest(TestCase):
    def setUp(self):
        Cart.objects.create()
        Product.objects.create(product_name="Courgettes", price_ht=1.05, stock_available=8, stock_ordered=0, tva=5.50)
        Item.objects.create(cart_id=Cart.objects.get(id=1), product_id=Product.objects.get(id=1), quantity=2)

    def test_cart(self):
        item = Item.objects.get(cart_id=1)
        self.assertEqual(item.cart_id.id, 1)
        self.assertEqual(item.product_id.id, 1)
