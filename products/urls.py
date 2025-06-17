from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.CategoryListAPIView.as_view(), name='category-list'),
    path('products/', views.ProductListAPIView.as_view(), name='product-list'),
    path('flash-sales/', views.FlashSaleListAPIView.as_view(), name='flash-sale-list'),
    path('promotions/', views.PromotionListAPIView.as_view(), name='promotion-list'),
    path('orders/', views.OrderListAPIView.as_view(), name='order-list'),
    path('signup/', views.UserSignupAPIView.as_view(), name='user-signup'),
]