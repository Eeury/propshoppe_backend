from django.contrib import admin
<<<<<<< HEAD
from .models import Category, Product, ProductImage, FlashSale, Promotion

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1 
    fields = ['image'] 
=======
from .models import Category, Product, FlashSale, Promotion
>>>>>>> 5c8dcb07b54a7f40de51739762ee08399ce646af

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']  
    list_filter = ['created_at']  

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
<<<<<<< HEAD
    list_display = ['name', 'price', 'category', 'created_at']
    list_filter = ['category', 'created_at']
    search_fields = ['name', 'description']
    fields = ['name', 'description', 'price', 'image', 'category', 'images']  
    inlines = [ProductImageInline]  
    readonly_fields = ['created_at']  
=======
    list_display = ['name', 'price', 'category', 'created_at', 'description']

>>>>>>> 5c8dcb07b54a7f40de51739762ee08399ce646af
@admin.register(FlashSale)
class FlashSaleAdmin(admin.ModelAdmin):
    list_display = ['product', 'discount_price', 'start_time', 'end_time', 'is_active']
    list_filter = ['start_time', 'end_time']

@admin.register(Promotion)
class PromotionAdmin(admin.ModelAdmin):
<<<<<<< HEAD
    list_display = ['name', 'discount_percentage', 'start_date', 'end_date', 'is_active']
    list_filter = ['start_date', 'end_date']
    search_fields = ['name', 'description']
=======
    list_display = ['name', 'discount_percentage', 'start_date', 'end_date']
>>>>>>> 5c8dcb07b54a7f40de51739762ee08399ce646af
