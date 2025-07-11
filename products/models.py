<<<<<<< HEAD
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Added unique
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "Categories"  # Better admin display
        
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/%Y/%m/%d/', null=True, blank=True)  # Better upload path
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} (${self.price})"  # More descriptive

class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/%Y/%m/%d/')  # Date-based organization
    alt_text = models.CharField(max_length=125, blank=True)  # Added for accessibility
    
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

    def is_active(self):
        from django.utils import timezone
        now = timezone.now()
        return self.start_time <= now <= self.end_time

=======
>>>>>>> 5c8dcb07b54a7f40de51739762ee08399ce646af
class Promotion(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    discount_percentage = models.IntegerField(default=0)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def is_active(self):
        from django.utils import timezone
        now = timezone.now()
<<<<<<< HEAD
        return self.start_date <= now <= self.end_date
    
=======
        return self.start_date <= now <= self.end_date 
>>>>>>> 5c8dcb07b54a7f40de51739762ee08399ce646af
