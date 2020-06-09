from django.shortcuts import render, redirect
from django.http import HttpRequest
from .forms import CategoriesForm
from .forms import CustomersForm
from .forms import ProductsForm
from .models import Category
from .models import Customer
from .models import Product
from django.template import RequestContext
from datetime import datetime

# Create your views here.

def home(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/home/index.html'
    )

def categories_index(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/categories/index.html',
        {
            'categories': Category.objects.all()
        }
    )

def categories_add(request):
    assert isinstance(request, HttpRequest)
    if request.method == "GET":
        form = CategoriesForm()
        return render(
            request,
            'app/categories/add.html',
            {
                'form': form
            }
        )
    else:
        form = CategoriesForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/categories')

def categories_edit(request, id):
    assert isinstance(request, HttpRequest)
    if request.method == "GET":
        if id == 0:
            form = CategoriesForm()
        else:
            category = Category.objects.get(pk=id)
            form = CategoriesForm(instance=category)
        return render(
            request,
            'app/categories/edit.html',
            {
                'form': form
            }
        )
    else:
        if id == 0:
            form = CategoriesForm(request.POST)
        else:
            category = Category.objects.get(pk=id)
            form = CategoriesForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
        return redirect('/categories')


def categories_delete(request, id):
    category = Category.objects.get(pk=id)
    category.delete()
    return redirect('/categories')

def customers_index(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/customers/index.html',
        {
            'customers': Customer.objects.all()
        }
    )

def customers_add(request):
    assert isinstance(request, HttpRequest)
    if request.method == "GET":
        form = CustomersForm()
        return render(
            request,
            'app/customers/add.html',
            {
                'form': form
            }
        )
    else:
        form = CustomersForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/customers')

def customers_edit(request, id):
    assert isinstance(request, HttpRequest)
    if request.method == "GET":
        if id == 0:
            form = CustomersForm()
        else:
            customer = Customer.objects.get(pk=id)
            form = CustomersForm(instance=customer)
        return render(
            request,
            'app/customers/edit.html',
            {
                'form': form
            }
        )
    else:
        if id == 0:
            form = CustomersForm(request.POST)
        else:
            customer = Customer.objects.get(pk=id)
            form = CustomersForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
        return redirect('/customers')

def customers_delete(request, id):
    customer = Customer.objects.get(pk=id)
    customer.delete()
    return redirect('/customers')

def products_index(request):
    assert isinstance(request,HttpRequest)
    return render(
        request,
        'app/products/index.html',
        {
            'products': Product.objects.all()
        }
    )

def products_add(request):
    assert isinstance(request,HttpRequest)
    if request.method == "GET":
        form = ProductsForm()
        return render(
            request,
            'app/products/add.html',
            {
                'form':form
            }
        )
    else:
        form = ProductsForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/products')

def products_edit(request, id):
    assert isinstance(request,HttpRequest)
    if request.method == "GET":
        if id == 0:
            form = ProductsForm()
        else:
            product = Product.objects.get(pk=id)
            form = ProductsForm(instance=product)
        return render(
            request,
            'app/products/edit.html',
            {
                'form': form
            }
        )
    else:
        if id ==0:
            form = ProductsForm(request.POST)
        else:
            product = Product.objects.get(pk=id)
            form = ProductsForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
        return redirect('/products')

def products_delete(request, id):
    product = Product.objects.get(pk=id)
    product.delete()
    return redirect('/products')