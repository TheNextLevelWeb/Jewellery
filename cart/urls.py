from django.urls import path
from .views import CartView

urlpatterns = [
    path("cart/<str:username>/",CartView.as_view(),name="cart"),
    path("cart/remove/<int:pk>/",
         CartView.as_view(), name="delete-cart"),
]
