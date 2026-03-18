from django.db import models

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    ]

    DELIVERY_CHOICES = [
        ('delivery', 'Delivery'),
        ('pickup', 'Pickup'),
    ]

    # Customer Info
    full_name = models.CharField(max_length=200)
    contact_number = models.CharField(max_length=20)
    email = models.EmailField()

    # Order Info
    product_name = models.CharField(max_length=200)
    size = models.CharField(max_length=20)
    quantity = models.IntegerField(default=1)

    # Delivery Info
    delivery_option = models.CharField(max_length=20, choices=DELIVERY_CHOICES)
    delivery_address = models.TextField(blank=True)
    special_instructions = models.TextField(blank=True)

    # Status
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.product_name}"