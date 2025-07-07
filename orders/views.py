from django.shortcuts import render

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Order
from .serializers import OrderSerializer
from products.models import Product

class OrderListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = OrderSerializer
    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

class OrderCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = OrderSerializer
    def perform_create(self, serializer):
        product_id = self.request.data.get('product_id')
        quantity = self.request.data.get('quantity', 1)
        product = Product.objects.get(id=product_id)
        serializer.save(user=self.request.user, product=product, quantity=quantity)
