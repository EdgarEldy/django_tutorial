from django.http import HttpRequest
from django.shortcuts import redirect, render
from app.models import Product
from app.forms import ProductForm

# get produts list
def index(request):
    assert isinstance(request, HttpRequest)
    products = Product.objects.all()
    return render(
        request,
        'app/products/index.html',
        {
            'products': products
        }
    )

# Display new product form
def add(request):
    assert isinstance(request, HttpRequest)
    if request.method == 'GET':
        form = ProductForm
    return render(
        request,
        'app/products/add.html',
        {
            'form': form
        }
    )