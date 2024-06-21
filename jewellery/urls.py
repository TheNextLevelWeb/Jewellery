from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls'), name="users"),
    path('', include('shop.urls'), name="shop"),
    path('', include('notification_history.urls'), name="notification-history"),
    path('', include('feedback.urls'), name="feedback"),
    path('', include('rating.urls'), name="rating"),
    path('', include('coupon.urls'), name="coupon"),
    path('', include('FAQs.urls'), name="FAQs"),
    path('', include('NearByStores.urls'), name="NearByStores"),
    path('', include('supports.urls'), name="supports"),
    path('', include('cart.urls'), name="cart"),
    path('', include('rewards.urls'), name="rewards"),
    path('', include('giftcard.urls'), name="giftcard"),
]
