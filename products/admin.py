from django.contrib import admin
from .models import Category, Product, ProductImage, FlashSale, Promotion
import cloudinary.uploader

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
    fields = ['image', 'alt_text']

    def delete_model(self, request, obj):
        if obj.image:
            try:
                cloudinary.uploader.destroy(obj.image.public_id)
            except Exception as e:
                self.message_user(request, f"Error deleting Cloudinary image: {e}", level='error')
        super().delete_model(request, obj)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    list_filter = ['created_at']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category', 'created_at']
    list_filter = ['category', 'created_at']
    search_fields = ['name', 'description']
    fields = ['name', 'description', 'price', 'image', 'category']
    inlines = [ProductImageInline]
    readonly_fields = ['created_at']

    def delete_model(self, request, obj):
        if obj.image:
            try:
                cloudinary.uploader.destroy(obj.image.public_id)
            except Exception as e:
                self.message_user(request, f"Error deleting Cloudinary image: {e}", level='error')
        super().delete_model(request, obj)

    def delete_queryset(self, request, queryset):
        for obj in queryset:
            if obj.image:
                try:
                    cloudinary.uploader.destroy(obj.image.public_id)
                except Exception as e:
                    self.message_user(request, f"Error deleting Cloudinary image for {obj.name}: {e}", level='error')
        super().delete_queryset(request, queryset)

@admin.register(FlashSale)
class FlashSaleAdmin(admin.ModelAdmin):
    list_display = ['product', 'discount_price', 'start_time', 'end_time', 'is_active']
    list_filter = ['start_time', 'end_time']
    fields = ['product', 'discount_price', 'start_time', 'end_time', 'image', 'alt_text']
    readonly_fields = ['is_active']

    def delete_model(self, request, obj):
        if obj.image:
            try:
                cloudinary.uploader.destroy(obj.image.public_id)
            except Exception as e:
                self.message_user(request, f"Error deleting Cloudinary image: {e}", level='error')
        super().delete_model(request, obj)

@admin.register(Promotion)
class PromotionAdmin(admin.ModelAdmin):
    list_display = ['name', 'discount_percentage', 'start_date', 'end_date', 'is_active']
    list_filter = ['start_date', 'end_date']
    search_fields = ['name', 'description']
    fields = ['name', 'description', 'discount_percentage', 'start_date', 'end_date', 'image', 'alt_text']
    readonly_fields = ['is_active']

    def delete_model(self, request, obj):
        if obj.image:
            try:
                cloudinary.uploader.destroy(obj.image.public_id)
            except Exception as e:
                self.message_user(request, f"Error deleting Cloudinary image: {e}", level='error')
        super().delete_model(request, obj)