
from django.db import models
from django.contrib.auth.models import User
from products.models import Product

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    phone = models.CharField(max_length=20, blank=True, null=True)  # Added
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Added
    mpesa_receipt = models.CharField(max_length=100, blank=True, null=True)  # Added
    status = models.CharField(max_length=50, default='pending')
    payment_status = models.CharField(max_length=50, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} by {self.user}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"