from django.urls import path
from .views import GiftCardView

urlpatterns = [
    path("giftcard/<str:code>/", GiftCardView.as_view(), name="GiftCardV")
]
