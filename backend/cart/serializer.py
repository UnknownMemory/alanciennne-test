from rest_framework import serializers

from .models import Cart, Item
from product.serializers import ProductSerializer


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ["cart_id", "product_id", "quantity", "total_price"]


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ["id", "checked_out", "total_cart"]
