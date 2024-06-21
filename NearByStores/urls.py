from django.urls import path 
from .views import NearByStoreView

urlpatterns = [
    path("NearByStore/", NearByStoreView.as_view(), name="Near_by_store"),
    path("NearByStore/<int:pk>/", NearByStoreView.as_view(), name="delete-update-Near_by_store")
]
