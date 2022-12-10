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
    
# Save a new customer
def store(request):
    assert isinstance(request, HttpRequest)
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
        
        messages.success(request, "Customer has been saved successfully !")
            
        return redirect('/customers')
    
# Edit a customer
def edit(request, id):
    assert isinstance(request, HttpRequest)
    if request.method == 'GET':
        if id == 0:
            form = CustomerForm()
        else:
            customer = Customer.objects.get(pk=id)
            form = CustomerForm(instance=customer)
        return render(
            request,
            'app/customers/edit.html',
            {
                'form': form
            }
        )
        
    # Update a customer
def update(request, id):
    if request.method == 'POST':
        if id == 0:
            form = CustomerForm(request.POST)
        else:
            customer = Customer.objects.get(pk=id)
            form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
        messages.success(request, "Customer has been updated successfully !")
        return redirect('/customers')
    
# Remove a customer    
def delete(request, id):
    customer = Customer.objects.get(pk=id)
    customer.delete()
    messages.success(request, "Customer has been removed successfully !")
    return redirect('/customers')