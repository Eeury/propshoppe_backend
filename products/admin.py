from django.contrib import admin
from .models import Category, Product, ProductImage, FlashSale, Promotion

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1 
    fields = ['image'] 

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']  
    list_filter = ['created_at']  

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category', 'created_at']
    list_filter = ['category', 'created_at']
    search_fields = ['name', 'description']
    fields = ['name', 'description', 'price', 'image', 'category', 'images']  
    inlines = [ProductImageInline]  
    readonly_fields = ['created_at']  
@admin.register(FlashSale)
class FlashSaleAdmin(admin.ModelAdmin):
    list_display = ['product', 'discount_price', 'start_time', 'end_time', 'is_active']
    list_filter = ['start_time', 'end_time']

@admin.register(Promotion)
class PromotionAdmin(admin.ModelAdmin):
    list_display = ['name', 'discount_percentage', 'start_date', 'end_date', 'is_active']
    list_filter = ['start_date', 'end_date']
    search_fields = ['name', 'description']
