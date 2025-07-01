from django.contrib import admin
from .models import PaymentTransaction

@admin.register(PaymentTransaction)
class PaymentTransactionAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "phone",
        "amount",
        "status",
        "timestamp",
        "user",
        "checkout_request_id",
        "mpesa_receipt"
    )
    search_fields = ("phone", "checkout_request_id", "mpesa_receipt")
    list_filter = ("status", "timestamp")
