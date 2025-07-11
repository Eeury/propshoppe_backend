
from django.contrib import admin
from .models import Order, OrderItem

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'phone', 'total_amount', 'status', 'mpesa_receipt', 'created_at']
    search_fields = ['user__username', 'phone', 'mpesa_receipt']
    list_filter = ['status', 'created_at']

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'quantity']
    search_fields = ['order__id', 'product__name']