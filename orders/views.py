from django.shortcuts import render, redirect
from .models import Order

def order_form(request):
    if request.method == 'POST':
        Order.objects.create(
            full_name = request.POST['full_name'],
            contact_number = request.POST['contact_number'],
            email = request.POST['email'],
            product_name = request.POST['product_name'],
            size = request.POST['size'],
            quantity = request.POST['quantity'],
            delivery_option = request.POST['delivery_option'],
            delivery_address = request.POST.get('delivery_address', ''),
            special_instructions = request.POST.get('special_instructions', ''),
        )
        return redirect('order_success')
    return render(request, 'order_form.html')

def order_success(request):
    return render(request, 'order_success.html')