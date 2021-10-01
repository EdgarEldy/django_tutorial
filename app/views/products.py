from django.http import HttpRequest
from django.shortcuts import render, redirect
from app.models import Category, Product
from app.forms import ProductsForm


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
