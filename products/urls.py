from .views import (
    CustomAuthToken,
    CategoryListAPIView,
    ProductListAPIView,
    ProductDetailAPIView,
    FlashSaleListAPIView,
    PromotionListAPIView,
    UserSignupAPIView,
    ProtectedTestView,
)
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path('categories/', CategoryListAPIView.as_view(), name='category-list'),
    path('', ProductListAPIView.as_view(), name='product-list'),  
    path('<int:pk>/', ProductDetailAPIView.as_view(), name='product-detail'), 
    path('flash-sales/', FlashSaleListAPIView.as_view(), name='flash-sale-list'),
    path('promotions/', PromotionListAPIView.as_view(), name='promotion-list'),
<<<<<<< HEAD
    path('orders/create/', CreateOrderView.as_view(), name='order-create'),
=======
>>>>>>> 5c8dcb07b54a7f40de51739762ee08399ce646af
    path('signup/', UserSignupAPIView.as_view(), name='user-signup'),
    path('token-auth/', CustomAuthToken.as_view(), name='token-auth'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('protected/', ProtectedTestView.as_view(), name='protected-test'),
]