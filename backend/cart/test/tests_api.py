import json
from django.urls import reverse
from rest_framework.test import APITestCase

from ..models import Cart, Item
from product.models import Product


class CartAPITest(APITestCase):
    def test_create_cart(self):
        url = reverse("create-cart")
        response = self.client.post(url)
        data = json.loads(response.content)

        self.assertEqual(data["id"], 1)

    def test_get_cart(self):
        self.client.post(reverse("create-cart"))
        url = reverse("get-cart", args=[1])
        response = self.client.get(url)
        data = json.loads(response.content)

        self.assertEqual(data["id"], 1)

    def test_update_cart(self):
        self.client.post(reverse("create-cart"))
        url = reverse("checked-out", args=[1])
        response = self.client.put(url, data={"checked_out": True})
        data = json.loads(response.content)

        self.assertEqual(data["checked_out"], True)


class ItemAPITest(APITestCase):
    def setUp(self):
        Product.objects.create(product_name="Courgettes", price_ht=1.05, stock_available=8, stock_ordered=0, tva=5.50)
        Product.objects.create(product_name="Carottes", price_ht=1.20, stock_available=4, stock_ordered=0, tva=5.50)
        Cart.objects.create()
        Item.objects.create(cart_id=Cart.objects.get(id=1), product_id=Product.objects.get(id=1), quantity=2)
        Item.objects.create(cart_id=Cart.objects.get(id=1), product_id=Product.objects.get(id=2), quantity=2)

    def test_get_items(self):
        url = reverse("get-items", args=[1])
        response = self.client.get(url)
        data = json.loads(response.content)

        print(data)

        self.assertEqual(len(data), 2)
