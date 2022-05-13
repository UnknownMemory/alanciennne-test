from rest_framework import generics

from .models import Cart, Item
from .serializer import CartSerializer, ItemSerializer

# Crée le panier
class CreateCart(generics.CreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


# Clôture le panier
class UpdateCart(generics.UpdateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


# Récupère le panier
class GetCart(generics.RetrieveAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


# Ajoute un produit dans un panier
class AddItem(generics.CreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
