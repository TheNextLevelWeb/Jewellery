from django.urls import path
from .views import CouponView, CouponCheckView

#Delete and adding coupon should be done from Admin dashboard

# path('coupon/delete/<str:code>/',
#      CouponView.as_view(), name='deletePromocode'),
# path('coupon/add/', CouponView.as_view(), name='Add-coupon '),
urlpatterns = [
    path('coupon/list/', CouponView.as_view(), name='List-coupons'),
    path('coupon/check/', CouponCheckView.as_view(), name='checkPromocode'),
]
