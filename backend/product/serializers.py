from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "product_name", "price_ht", "stock_available", "stock_ordered", "tva", "price_ttc"]
