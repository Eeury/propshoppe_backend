
from django.urls import path
from .views import (
    CategoryListAPIView,
    ProductListAPIView,
    ProductDetailAPIView,
    FlashSaleListAPIView,
    PromotionListAPIView,
)

urlpatterns = [
    path('categories/', CategoryListAPIView.as_view(), name='category-list'),
    path('products/', ProductListAPIView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailAPIView.as_view(), name='product-detail'),
    path('flash-sales/', FlashSaleListAPIView.as_view(), name='flash-sale-list'),
    path('promotions/', PromotionListAPIView.as_view(), name='promotion-list'),
]