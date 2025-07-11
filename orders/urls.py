from django.urls import path
from . import views

urlpatterns = [
   path('orders/', views.OrderViewSet.as_view({'get': 'list', 'post': 'create'})),
   path('payments/orders/create/', views.OrderCreateView.as_view(), name='order-create'),
]