from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "id",
            "product_name",
            "stock_available",
            "stock_ordered",
            "price_ttc",
            "customer_stock",
        ]
        read_only_fields = ["id", "product_name", "stock_available", "price_ttc", "customer_stock"]

    def update(self, instance, validated_data):
        new_stock = validated_data.get("stock_ordered", instance.stock_ordered) + instance.stock_ordered

        if new_stock <= instance.stock_available:
            instance.stock_ordered = new_stock

        instance.save()
        return instance
