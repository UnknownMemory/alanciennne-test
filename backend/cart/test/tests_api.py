import json
from django.urls import reverse
from rest_framework.test import APITestCase

from ..models import Cart, Item


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
