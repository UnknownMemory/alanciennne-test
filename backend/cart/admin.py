from django.contrib import admin

from .models import Cart, Item


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ("id", "total_cart")


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("id", "cart_id", "product_id", "quantity", "total_price")
