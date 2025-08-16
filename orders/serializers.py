from rest_framework import serializers
from .models import Order, OrderItem
from products.serializers import ProductSerializer

class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    class Meta:
        model = OrderItem
        fields = ['product', 'quantity']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True, source='orderitem_set')
    product = ProductSerializer(read_only=True)  
    class Meta:
        model = Order
        fields = ['id', 'user', 'phone', 'total_amount', 'status', 'payment_status', 'items', 'created_at', 'product', 'quantity']