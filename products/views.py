from django.shortcuts import render, get_object_or_404
from .models import Product

def home(request):
    featured = Product.objects.filter(is_available=True)[:9]
    return render(request, 'home.html', {'featured': featured})

def products(request):
    category = request.GET.get('category', None)
    if category:
        items = Product.objects.filter(is_available=True, category=category)
    else:
        items = Product.objects.filter(is_available=True)
    return render(request, 'products.html', {'items': items})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    model_photos = product.model_photos.all()
    return render(request, 'product_detail.html', {
        'product': product,
        'model_photos': model_photos
    })