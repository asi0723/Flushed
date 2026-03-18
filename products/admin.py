from django.contrib import admin
from .models import Product, ProductModelPhoto

class ProductModelPhotoInline(admin.TabularInline):
    model = ProductModelPhoto
    extra = 3

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'stock', 'is_available']
    list_filter = ['category', 'is_available']
    search_fields = ['name']
    list_editable = ['price', 'stock', 'is_available']
    inlines = [ProductModelPhotoInline]