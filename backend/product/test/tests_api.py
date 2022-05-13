from cgitb import reset
import json
from django.urls import reverse
from rest_framework.test import APITestCase

from ..models import Product


class ProductAPITest(APITestCase):
    def setUp(self):
        Product.objects.create(product_name="Courgettes", price_ht=1.05, stock_available=8, stock_ordered=0, tva=5.50)
        Product.objects.create(product_name="Carottes", price_ht=1.20, stock_available=4, stock_ordered=0, tva=5.50)

    def test_get_products(self):
        url = reverse("product-list")
        response = self.client.get(url)
        data = json.loads(response.content)

        self.assertEqual(len(data), 2)
