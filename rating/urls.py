from django.urls import path
from .views import RatingView

urlpatterns = [
    path("rating/<str:product>/",RatingView.as_view(),name="ratings"),
    path("rating/delete/<int:pk>/",RatingView.as_view(),name="delete-rating"),
    path("rating/update/<int:pk>/",RatingView.as_view(),name="update-rating")
]
