from django.shortcuts import render
from .models import Product

def list(request):
    Data = {'Products' :Product.objects.all().order_by('-created_at')}
    return render(request, 'pages/products.html', Data)
# Create your views here.

def product(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'pages/details.html', {'product' : product})