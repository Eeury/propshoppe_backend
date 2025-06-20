
from django.db import models

class Product(models.Model):  
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

class PaymentTransaction(models.Model):
    phone = models.CharField(max_length=15)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    mpesa_receipt = models.CharField(max_length=100, blank=True, null=True)
    checkout_request_id = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=20, default="Pending")  
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.phone} - {self.amount} - {self.status}"
