from django.db import models
from cloudinary.models import CloudinaryField
from django.core.validators import FileExtensionValidator

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image = CloudinaryField(
        'image',
        folder='categories',
        null=True,
        blank=True,
        default='categories/placeholder',
        allowed_formats=['jpg', 'jpeg', 'png', 'gif']
    )
    
    class Meta:
        verbose_name_plural = "Categories"
        
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = CloudinaryField(
        'image',
        folder='products',
        null=True,
        blank=True,
        default='products/placeholder',
        allowed_formats=['jpg', 'jpeg', 'png', 'gif']
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} (${self.price})"

class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = CloudinaryField(
        'image',
        folder='product_images',
        allowed_formats=['jpg', 'jpeg', 'png', 'gif']
    )
    alt_text = models.CharField(max_length=125, blank=True)
    
    class Meta:
        verbose_name = "Product Image"
        verbose_name_plural = "Product Images"
    
    def __str__(self):
        return f"Image #{self.id} for {self.product.name}"

class FlashSale(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    image = CloudinaryField(
        'image',
        folder='flashsales',
        null=True,
        blank=True,
        default='flashsales/placeholder',
        allowed_formats=['jpg', 'jpeg', 'png', 'gif']
    )
    alt_text = models.CharField(max_length=125, blank=True)
    
    def is_active(self):
        from django.utils import timezone
        now = timezone.now()
        return self.start_time <= now <= self.end_time

class Promotion(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    discount_percentage = models.IntegerField(default=0)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    image = CloudinaryField(
        'image',
        folder='promotions',
        null=True,
        blank=True,
        default='promotions/placeholder',
        allowed_formats=['jpg', 'jpeg', 'png', 'gif']
    )
    alt_text = models.CharField(max_length=125, blank=True)
    
    def is_active(self):
        from django.utils import timezone
        now = timezone.now()
        return self.start_date <= now <= self.end_date