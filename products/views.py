from django.shortcuts import render, get_object_or_404
from .models import Product
from .models import Product, LookbookPhoto


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
    
def about(request):
    return render(request, 'about.html')

def lookbook(request):
    return render(request, 'lookbook.html')

def lookbook(request):
    collection = request.GET.get('collection', None)
    if collection:
        photos = LookbookPhoto.objects.filter(collection=collection).order_by('-created_at')
    else:
        photos = LookbookPhoto.objects.all().order_by('-created_at')
    return render(request, 'lookbook.html', {'photos': photos})

def contact(request):
    return render(request, 'contact.html')

def contact(request):
    if request.method == 'POST':
        submitted = True
        return render(request, 'contact.html', {'submitted': submitted})
    return render(request, 'contact.html')