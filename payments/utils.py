import requests
from django.conf import settings
from requests.auth import HTTPBasicAuth

def get_access_token():
    url = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
    res = requests.get(url, auth=HTTPBasicAuth(settings.CONSUMER_KEY, settings.CONSUMER_SECRET))
    return res.json().get("access_token")
