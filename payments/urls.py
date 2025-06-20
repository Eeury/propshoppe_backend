
from django.urls import path
from . import views

urlpatterns = [
    path("stkpush/", views.stk_push),
    path("callback/", views.stk_callback),
    path("mpesa/callback/", views.mpesa_callback, name="mpesa_callback"),
    path("payment/status/", views.payment_status, name="payment_status"),
]

