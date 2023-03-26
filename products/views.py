from django.shortcuts import render
from .models import Product, ProductCategory
# Create your views here.
def index(request):
    context = {
        'title': 'store'
    }
    return render(request, 'products/index.html', context)

def products(request):
    context = {
        'title': 'store - каталог',
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all(),
    }
    return render(request, 'products/products.html', context)