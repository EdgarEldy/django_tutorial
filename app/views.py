from django.shortcuts import render, redirect
from django.http import HttpRequest
from .forms import *
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from datetime import datetime


# Create your views here.

@login_required(login_url='users_login')
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
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/products/index.html',
        {
            'products': Product.objects.all()
        }
    )


def products_add(request):
    assert isinstance(request, HttpRequest)
    if request.method == "GET":
        form = ProductsForm()
        return render(
            request,
            'app/products/add.html',
            {
                'form': form
            }
        )
    else:
        form = ProductsForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/products')


def products_edit(request, id):
    assert isinstance(request, HttpRequest)
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
        if id == 0:
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


def orders_index(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/orders/index.html',
        {
            'orders': Order.objects.all()
        }
    )


def orders_add(request):
    assert isinstance(request, HttpRequest)
    if request.method == "GET":
        form = OrdersForm()
        return render(
            request,
            'app/orders/add.html',
            {
                'form': form,
                'categories': Category.objects.all()
            }
        )
    else:
        form = OrdersForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/orders')


# Getting products by category_id
def getProducts(request):
    category_id = request.GET.get('category_id')
    products = Product.objects.filter(category_id=category_id).order_by('product_name')
    return render(
        request,
        'app/orders/getProducts.html',
        {
            'products': products
        }
    )


def orders_edit(request, id):
    assert isinstance(request, HttpRequest)
    if request.method == "GET":
        if id == 0:
            form = OrdersForm()
        else:
            order = Order.objects.get(pk=id)
            form = OrdersForm(instance=order)
        return render(
            request,
            'app/orders/edit.html',
            {
                'form': form
            }
        )
    else:
        if id == 0:
            form = OrdersForm(request.POST)
        else:
            order = Order.objects.get(pk=id)
            form = OrdersForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
        return redirect('/orders')


def orders_delete(request, id):
    order = Order.objects.get(pk=id)
    order.delete()
    return redirect('/orders')


def users_index(request):
    assert isinstance(request, HttpRequest)
    users = User.objects.all()
    return render(
        request,
        'app/users/index.html',
        {
            'users': users
        }
    )


def users_add(request):
    assert isinstance(request, HttpRequest)
    if request.method == 'GET':
        form = UserForm()
        return render(
            request,
            'app/users/add.html',
            {
                'form': form
            }
        )
    else:
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/users')


def users_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Username or password is incorrect ! Please try again !')
    return render(
        request,
        'app/users/login.html'
    )


def users_logout(request):
    logout(request)
    return redirect('/users/login')
