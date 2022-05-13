from itertools import product
from django.db import models

from product.models import Product


class Cart(models.Model):
    checked_out = models.BooleanField(default=False)

    def total_cart(self):
        items = Item.objects.filter(cart_id=self.id)
        return sum(item.total_price() for item in items)


class Item(models.Model):
    cart_id = models.ForeignKey("Cart", on_delete=models.CASCADE)
    product_id = models.ForeignKey("product.Product", on_delete=models.CASCADE, related_name="product")
    quantity = models.PositiveIntegerField()

    class Meta:
        unique_together = ("cart_id", "product_id")

    def total_price(self):
        return self.product_id.price_ttc() * self.quantity
