from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import PaymentTransaction
from products.models import Product
from .utils import get_access_token
import requests
import json
import base64
from datetime import datetime


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def stk_push(request):
    data = request.data
    phone = data.get("phone")
    product_id = data.get("product_id")

    if not phone or not product_id:
        return Response({"error": "Phone and product_id are required"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        product = Product.objects.get(id=product_id)
        amount = int(float(product.price))
    except Product.DoesNotExist:
        return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    password = base64.b64encode((settings.SHORTCODE + settings.PASSKEY + timestamp).encode()).decode()

    access_token = get_access_token()
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = {"Authorization": f"Bearer {access_token}"}

    payload = {
        "BusinessShortCode": settings.SHORTCODE,
        "Password": password,
        "Timestamp": timestamp,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": amount,
        "PartyA": phone,
        "PartyB": settings.SHORTCODE,
        "PhoneNumber": phone,
        "CallBackURL": settings.CALLBACK_URL,
        "AccountReference": f"Product{product_id}",
        "TransactionDesc": f"Payment for {product.name}"
    }

    res = requests.post(api_url, json=payload, headers=headers)
    mpesa_response = res.json()

    if 'errorCode' in mpesa_response:
        return Response({"error": mpesa_response}, status=400)

    PaymentTransaction.objects.create(
        phone=phone,
        amount=amount,
        product=product,
        checkout_request_id=mpesa_response.get("CheckoutRequestID"),
        user=request.user
    )

    return Response(mpesa_response)


@csrf_exempt
def mpesa_callback(request):
    data = json.loads(request.body.decode('utf-8'))
    body = data.get("Body", {}).get("stkCallback", {})
    result_code = body.get("ResultCode")
    checkout_id = body.get("CheckoutRequestID")

    try:
        transaction = PaymentTransaction.objects.get(checkout_request_id=checkout_id)
    except PaymentTransaction.DoesNotExist:
        return JsonResponse({"error": "Transaction not found"}, status=404)

    if result_code == 0:
        metadata = body.get("CallbackMetadata", {})
        mpesa_receipt = next((item["Value"] for item in metadata.get("Item", []) if item["Name"] == "MpesaReceiptNumber"), None)
        amount = next((item["Value"] for item in metadata.get("Item", []) if item["Name"] == "Amount"), None)
        phone = next((item["Value"] for item in metadata.get("Item", []) if item["Name"] == "PhoneNumber"), None)

        transaction.status = "Success"
        transaction.mpesa_receipt = mpesa_receipt
        transaction.save()
    else:
        transaction.status = "Failed"
        transaction.save()

    return JsonResponse({"ResultCode": 0, "ResultDesc": "Accepted"})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def payment_status(request):
    phone = request.query_params.get("phone")

    if not phone:
        return Response({"error": "Phone number required"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        transaction = PaymentTransaction.objects.filter(
            phone=phone,
            user=request.user
        ).latest("timestamp")
    except PaymentTransaction.DoesNotExist:
        return Response({"status": "Not Found"})
    except Exception as e:
        return Response({"error": str(e)})

    return Response({
        "status": transaction.status,
        "product": transaction.product.name if transaction.product else None,
        "receipt": transaction.mpesa_receipt
    })
