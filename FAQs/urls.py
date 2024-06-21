from django.urls import path
from .views import FAQsView,PrivacyPolicyView

urlpatterns = [
    path("FAQs/",FAQsView.as_view(),name="FAQs"),
    path("FAQs/delete/<int:pk>/",FAQsView.as_view(),name="delete-FAQs"),
    path("FAQs/update/<int:pk>/",FAQsView.as_view(),name="update-FAQs"),
    path("PrivacyPolicy/", PrivacyPolicyView.as_view(), name="PrivacyPolicy"),
    path("PrivacyPolicy/delete/<int:pk>/",
         PrivacyPolicyView.as_view(), name="PrivacyPolicy-FAQs"),
    path("PrivacyPolicy/update/<int:pk>/",
         PrivacyPolicyView.as_view(), name="PrivacyPolicy-FAQs"),

]