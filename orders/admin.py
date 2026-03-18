from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'product_name', 'size', 'quantity', 'delivery_option', 'status', 'created_at']
    list_filter = ['status', 'delivery_option']
    search_fields = ['full_name', 'product_name', 'contact_number']
    list_editable = ['status']