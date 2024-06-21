from django.urls import path, include
from users.views import Register, LoginView, TokenAuthenticationView, ChangePassword, ForgotPasswordView, SOWListView, ProfileView

urlpatterns = [
    path('register/', Register.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('authenticate/', TokenAuthenticationView.as_view(),
            name='authenticate'),
    path('change_password/', ChangePassword.as_view(),
            name='change_password'),
    path('forgot/', ForgotPasswordView.as_view(),
            name='forgot'),
    path('users/<str:fieldName>/<str:username>/',
         SOWListView.as_view(), name='F'),
    path('profile/<str:username>/', ProfileView.as_view(), name='profile')

]
