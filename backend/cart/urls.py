from django.urls import path, re_path

from . import views

urlpatterns = [
    path("create/", views.CreateCart.as_view(), name="create-cart"),
    path("add-item/", views.AddItem.as_view(), name="add-item"),
    path("get/<int:pk>/", views.GetCart.as_view(), name="get-cart"),
    path("check-out/<int:pk>/", views.UpdateCart.as_view(), name="checked-out"),
    path("<int:cart_id>/items/", views.GetItems.as_view(), name="get-items"),
    path("<int:pk>/update-item/", views.UpdateItem.as_view(), name="update-item"),
]
