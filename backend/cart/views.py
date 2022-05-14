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


# Récupère la liste des produits d'un panier
class GetItems(generics.ListAPIView):
    serializer_class = ItemSerializer

    def get_queryset(self):
        cart_id = self.kwargs["cart_id"]
        return Item.objects.filter(cart_id=cart_id)


# Mets à jour un produit du panier
class UpdateItem(generics.UpdateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
