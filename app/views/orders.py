from django.http import HttpRequest
from django.shortcuts import render, redirect
from app.models import Order, Product, Category
from app.forms import OrdersForm

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

# Getting unit_price by id_product
def getUnitPrice(request):
    id_product = request.GET.get('id_product')
    product = Product.objects.get(pk=id_product)
    return render(
        request,
        'app/orders/getUnitPrice.html',
        {
            'product': product
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