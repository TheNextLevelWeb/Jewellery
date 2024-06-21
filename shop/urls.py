from django.urls import path, include
from shop.views import CategoryView, ProductView, ProductList

urlpatterns = [
    path('categories/', CategoryView.as_view(), name='categories'),
    path('categories/<int:pk>/', CategoryView.as_view(), name='update-category'),
    path('products/', ProductView.as_view(), name='categories'),
    path('products/<int:pk>/', ProductView.as_view(), name='update-category'),
    path('searchProduct/', ProductList.as_view(), name='product-searching'),
]
