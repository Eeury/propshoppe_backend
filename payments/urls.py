from django.urls import path
from . import views

urlpatterns = [
    path("payment/stkpush/", views.stk_push),
    path("payment/callback/", views.mpesa_callback, name="mpesa_callback"),
    path("payment/status/", views.payment_status, name="payment_status"),
]