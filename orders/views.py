from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Order, OrderItem
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
        items = self.request.data.get('items', [])
        total_amount = 0
        order = serializer.save(user=self.request.user, phone=self.request.data.get('phone', ''), county=self.request.data.get('county', ''), town=self.request.data.get('town', ''))
        for item in items:
            product = Product.objects.get(id=item['product_id'])
            quantity = item.get('quantity', 1)
            total_amount += product.price * quantity
            OrderItem.objects.create(order=order, product=product, quantity=quantity)
        order.total_amount = total_amount
        order.save()