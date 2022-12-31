from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.contrib import messages

from app.models import Order, Category
from app.forms import OrderForm
# Show orders list
def index(request):
    assert isinstance(request, HttpRequest)
    orders = Order.objects.all()
    return render(
        request,
        'app/orders/index.html',
        {
            'orders': orders
        }
    )
    
# Get orders page with categories
def add(request):
    assert isinstance(request, HttpRequest)
    categories = Category.objects.all()
    form = OrderForm()
    return render(
        request,
        'app/orders/add.html',
        {
            'form': form,
            'categories': categories
        }
    )