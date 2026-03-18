from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('hoodie', 'Hoodie'),
        ('cap', 'Cap'),
        ('pants', 'Pants'),
        ('tshirt', 'T-Shirt'),
        ('shorts', 'Shorts'),
        ('hoodie_pants', 'Hoodie Pants'),
        ('accessories', 'Accessories'),
        ('gymfit', 'Gymfit'),
        ('sando', 'Sando'),
        ('tank_top', 'Tank Top'),
    ]

    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    sizes = models.CharField(max_length=100, blank=True)
    stock = models.IntegerField(default=0)
    is_available = models.BooleanField(default=True)
    main_image = models.ImageField(upload_to='products/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class ProductModelPhoto(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='model_photos'
    )
    photo = models.ImageField(upload_to='model_photos/')
    caption = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.product.name} - Model Photo"
    
    
class LookbookPhoto(models.Model):
    COLLECTION_CHOICES = [
        ('season1', 'Season 1'),
        ('season2', 'Season 2'),
        ('latest', 'Latest Drop'),
    ]

    photo = models.ImageField(upload_to='lookbook/')
    caption = models.CharField(max_length=200, blank=True)
    collection = models.CharField(max_length=100, choices=COLLECTION_CHOICES, default='latest')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Lookbook - {self.collection} - {self.id}"