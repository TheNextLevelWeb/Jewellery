from django.urls import path
from .views import RewardView

urlpatterns = [
    path('rewards/<str:username>/', RewardView.as_view(), name='lits-create_reward'),
]