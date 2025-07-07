from django.urls import path
from . import views

urlpatterns = [
    path('orders/', views.OrderListView.as_view(), name='order-list'),
    path('payments/orders/create/', views.OrderCreateView.as_view(), name='order-create'),
]