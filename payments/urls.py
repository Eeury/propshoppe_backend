from django.urls import path
from . import views

urlpatterns = [
    path("api/payment/stkpush/", views.stk_push),
    path("api/payment/callback/", views.mpesa_callback, name="mpesa_callback"),
    path("api/payment/status/", views.payment_status, name="payment_status"),
]