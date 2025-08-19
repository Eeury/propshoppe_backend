from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Product, Category, ProductImage, FlashSale, Promotion

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

class CategorySerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'image']

class ProductSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source='category', write_only=True
    )

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'image', 'category', 'category_id', 'created_at']

class ProductImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = ProductImage
        fields = ['id', 'product', 'image', 'alt_text']

class FlashSaleSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)
    product = ProductSerializer(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(), source='product', write_only=True
    )

    class Meta:
        model = FlashSale
        fields = ['id', 'product', 'product_id', 'discount_price', 'start_time', 'end_time', 'image', 'alt_text']

class PromotionSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = Promotion
        fields = ['id', 'name', 'description', 'discount_percentage', 'start_date', 'end_date', 'image', 'alt_text']