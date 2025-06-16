from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Category, Product, FlashSale, Promotion, Order
from .serializers import CategorySerializer, ProductSerializer, FlashSaleSerializer, PromotionSerializer, OrderSerializer

class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class FlashSaleListAPIView(generics.ListAPIView):
    queryset = FlashSale.objects.all()
    serializer_class = FlashSaleSerializer

class PromotionListAPIView(generics.ListAPIView):
    queryset = Promotion.objects.all()
    serializer_class = PromotionSerializer

class OrderListAPIView(generics.ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)
    
from . import serializers
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

class UserSignupAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer 

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'message': 'User created successfully',
                'token': token.key
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)