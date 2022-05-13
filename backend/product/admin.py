from django.contrib import admin

from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("product_name", "price_ht", "stock_available", "stock_ordered", "tva", "price_ttc")
