from django.db import models


class Product(models.Model):
    TVA_CHOICES = [(5.50, "5,5%"), (20.00, "20%")]

    product_name = models.CharField(max_length=100, unique=True)
    price_ht = models.DecimalField(max_digits=6, decimal_places=2)
    stock_available = models.PositiveIntegerField(default=0)
    stock_ordered = models.PositiveIntegerField(default=0)
    tva = models.DecimalField(choices=TVA_CHOICES, max_digits=4, decimal_places=2, default="5,5%")

    def __str__(self):
        return self.product_name

    def price_ttc(self):
        ttc = (self.tva / 100) * self.price_ht + self.price_ht
        return round(ttc, 2)

    def customer_stock(self):
        return self.stock_available - self.stock_ordered
