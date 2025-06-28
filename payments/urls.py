from django.urls import path
from . import views
from .views import stk_push, payment_status, mpesa_callback
urlpatterns = [
    path("payment/stkpush/", views.stk_push),
    path("payment/callback/", views.mpesa_callback, name="mpesa_callback"),
    path("payment/status/", views.payment_status, name="payment_status"),
]