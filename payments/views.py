from django.shortcuts import render
from products.models import Product
import json
import base64
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.conf import settings
from .utils import get_access_token
from .models import PaymentTransaction
import requests

@csrf_exempt
def stk_push(request):
    data = json.loads(request.body)
    phone = data.get("phone")
    product_id = data.get("product_id")

    if not phone or not product_id:
        return JsonResponse({"error": "Phone and product_id are required"}, status=400)

    # Step 1: Get product price from DB
    try:
        product = Product.objects.get(id=product_id)
        amount = int(float(product.price))
    except Product.DoesNotExist:
        return JsonResponse({"error": "Product not found"}, status=404)

    # Step 2: Generate password
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    password = base64.b64encode(
        (settings.SHORTCODE + settings.PASSKEY + timestamp).encode()
    ).decode()

    # Step 3: Get access token
    access_token = get_access_token()
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = {"Authorization": f"Bearer {access_token}"}

    # Step 4: Build payload
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

    PaymentTransaction.objects.create(
        phone=phone,
        amount=amount,
        product=product,
        checkout_request_id=mpesa_response.get("CheckoutRequestID")
    )

    return JsonResponse(mpesa_response)

@csrf_exempt
def stk_callback(request):
    data = json.loads(request.body)
    result = data.get("Body", {}).get("stkCallback", {})
    result_code = result.get("ResultCode")
    metadata = result.get("CallbackMetadata", {})

    phone = None
    amount = None
    mpesa_receipt = None

    if result_code == 0:
        for item in metadata.get("Item", []):
            if item["Name"] == "PhoneNumber":
                phone = item["Value"]
            elif item["Name"] == "Amount":
                amount = item["Value"]
            elif item["Name"] == "MpesaReceiptNumber":
                mpesa_receipt = item["Value"]

        PaymentTransaction.objects.filter(phone=phone, amount=amount).update(
            status="Success", mpesa_receipt=mpesa_receipt
        )
    else:
        # Mark as failed if needed
        pass

    return JsonResponse({"ResultCode": 0, "ResultDesc": "Accepted"})

@csrf_exempt
def payment_status(request):
    phone = request.GET.get("phone")

    if not phone:
        return JsonResponse({"error": "Phone number required"}, status=400)

    try:
        transaction = PaymentTransaction.objects.filter(phone=phone).latest("timestamp")
    except PaymentTransaction.DoesNotExist:
        return JsonResponse({"status": "Not Found"})

    return JsonResponse({
        "status": transaction.status,
        "product": transaction.product.name if transaction.product else None,
        "receipt": transaction.mpesa_receipt
    })

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
        # Payment was successful
        mpesa_receipt = body["CallbackMetadata"]["Item"][1]["Value"]
        transaction.status = "Success"
        transaction.mpesa_receipt = mpesa_receipt
    else:
        # Payment failed or was cancelled
        transaction.status = "Failed"

    transaction.save()
    return JsonResponse({"message": "Callback received successfully"})