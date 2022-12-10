from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.contrib import messages

# Import Customer model
from app.models import Customer
from app.forms import CustomerForm

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
    
# Get new customer's form
def add(request):
    assert isinstance(request, HttpRequest)
    if request.method == 'GET':
        form = CustomerForm
    return render(
        request,
        'app/customers/add.html',
        {
            'form': form
        }
    )