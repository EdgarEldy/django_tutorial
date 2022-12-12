from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.contrib import messages

from app.models import Order

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