from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.contrib import messages
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
    
# Save a new product
def store(request):
    assert isinstance(request, HttpRequest)
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
        
        messages.success(request, "Product has been saved successfully !")
            
        return redirect('/products')
    
# Edit a product
def edit(request, id):
    assert isinstance(request, HttpRequest)
    if request.method == 'GET':
        if id == 0:
            form = ProductForm()
        else:
            category = Product.objects.get(pk=id)
            form = ProductForm(instance=category)
        return render(
            request,
            'app/products/edit.html',
            {
                'form': form
            }
        )