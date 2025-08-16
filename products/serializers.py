from rest_framework import serializers
from .models import Category, Product, FlashSale, Promotion, ProductImage
from django.contrib.auth.models import User

class CategorySerializer(serializers.ModelSerializer):
    image = serializers.ImageField(allow_null=True, required=False)
    class Meta:
        model = Category
        fields = ['id', 'name', 'created_at', 'image']

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['image', 'alt_text']

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    images = ProductImageSerializer(many=True, read_only=True)
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'category', 'image', 'images', 'created_at']

class FlashSaleSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    image = serializers.ImageField(allow_null=True, required=False)
    class Meta:
        model = FlashSale
        fields = ['id', 'product', 'discount_price', 'start_time', 'end_time', 'is_active', 'image', 'alt_text']

class PromotionSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(allow_null=True, required=False)
    class Meta:
        model = Promotion
        fields = ['id', 'name', 'description', 'discount_percentage', 'start_date', 'end_date', 'is_active', 'image', 'alt_text']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user