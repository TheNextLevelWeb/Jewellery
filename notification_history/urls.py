from django.urls import path
from .views import NHView

urlpatterns = [
    path('notification_history/<str:username>/', NHView.as_view(),
         name='notification_history-list-create'),
    path('notification_history/<str:username>/<int:pk>/', NHView.as_view(),
         name='notification_history-delete'),
]
