from django.urls import path
from . import views

urlpatterns = [path("list/", views.GetProducts.as_view(), name="product-list")]
