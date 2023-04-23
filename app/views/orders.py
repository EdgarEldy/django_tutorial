from django.http import HttpRequest, JsonResponse
from django.shortcuts import redirect, render
from django.contrib import messages

from app.models import Order, Category, Product
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


# Get products by category id and convert into json
def getProducts(request):
    category_id = request.GET.get('category_id')
    products = Product.objects.filter(category_id=category_id).order_by('product_name').values()
    return JsonResponse(list(products), safe=False)


# Get unit price by product id
def getUnitPrice(request):
    id_product = request.GET.get('id_product')
    product = Product.objects.get(pk=id_product)
    # data = serialize("json", [product], fields=('unit_price'))
    return render(
        request,
        'app/orders/getUnitPrice.html',
        {
            'product': product
        }
    )
