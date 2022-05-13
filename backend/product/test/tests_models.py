from decimal import Decimal
from django.test import TestCase

from ..models import Product


class ProductTest(TestCase):
    def setUp(self):
        Product.objects.create(product_name="Courgettes", price_ht=1.05, stock_available=8, stock_ordered=0, tva=5.50)
        Product.objects.create(product_name="Carottes", price_ht=1.20, stock_available=4, stock_ordered=0, tva=5.50)

    def test_product(self):
        product_courgettes = Product.objects.get(product_name="Courgettes")
        product_carottes = Product.objects.get(product_name="Carottes")

        self.assertEqual(product_courgettes.price_ttc(), Decimal("1.11"))
        self.assertEqual(product_courgettes.stock_available, 8)
        self.assertEqual(product_carottes.price_ttc(), Decimal("1.27"))
        self.assertEqual(product_carottes.stock_available, 4)
