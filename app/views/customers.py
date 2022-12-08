from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.contrib import messages

# Import Customer model
from app.models import Customer

# Get customers list
def index(request):
    assert isinstance(request, HttpRequest)
    customers = Customer.objects.all()
    return render(
        request,
        'app/customers/index.html',
        {
            'customers': customers
        }
    )