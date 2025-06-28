from django.urls import path
from . import views
from .views import CustomAuthToken
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path('categories/', views.CategoryListAPIView.as_view(), name='category-list'),
    path('products/', views.ProductListAPIView.as_view(), name='product-list'),
    path('products/<int:pk>/', views.ProductDetailAPIView.as_view(), name='product-detail'),
    path('flash-sales/', views.FlashSaleListAPIView.as_view(), name='flash-sale-list'),
    path('promotions/', views.PromotionListAPIView.as_view(), name='promotion-list'),
    path('orders/', views.OrderListAPIView.as_view(), name='order-list'),
    path('signup/', views.UserSignupAPIView.as_view(), name='user-signup'),
    path('token-auth/', CustomAuthToken.as_view(), name='token-auth'),
    # JWT endpoints
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('protected/', views.ProtectedTestView.as_view(), name='protected-test'),

]
