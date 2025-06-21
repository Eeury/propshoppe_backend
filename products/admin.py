<<<<<<< HEAD
from django.contrib import admin
from .models import Category, Product, FlashSale, Promotion, Order

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category', 'created_at']

@admin.register(FlashSale)
class FlashSaleAdmin(admin.ModelAdmin):
    list_display = ['product', 'discount_price', 'start_time', 'end_time', 'is_active']

@admin.register(Promotion)
class PromotionAdmin(admin.ModelAdmin):
    list_display = ['name', 'discount_percentage', 'start_date', 'end_date', 'is_active']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
=======
from django.contrib import admin
from .models import Category, Product, FlashSale, Promotion, Order

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category', 'created_at']

@admin.register(FlashSale)
class FlashSaleAdmin(admin.ModelAdmin):
    list_display = ['product', 'discount_price', 'start_time', 'end_time', 'is_active']

@admin.register(Promotion)
class PromotionAdmin(admin.ModelAdmin):
    list_display = ['name', 'discount_percentage', 'start_date', 'end_date', 'is_active']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
>>>>>>> 431a0ee314690059840ecf1faf1e762be2d79575
    list_display = ['user', 'product', 'quantity', 'total_price', 'status', 'created_at']