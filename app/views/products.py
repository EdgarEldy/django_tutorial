from django.http import HttpRequest
from django.shortcuts import redirect, render
from app.models import Product

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
    