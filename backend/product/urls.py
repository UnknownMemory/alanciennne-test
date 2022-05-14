from django.urls import path
from . import views

urlpatterns = [
    path("list/", views.GetProducts.as_view(), name="product-list"),
    path("<int:pk>/", views.GetProduct.as_view(), name="get-product"),
    path("<int:pk>/update/", views.UpdateProduct.as_view(), name="update-product"),
]
