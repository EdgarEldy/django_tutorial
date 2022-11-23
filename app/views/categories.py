from django.http import HttpRequest
from django.shortcuts import render

from app.models import Category
from app.forms import CategoryForm

# Categories list
def index(request):
    assert isinstance(request, HttpRequest)
    categories = Category.objects.all()
    return render(
        request,
        'app/categories/index.html',
        {
            'categories': categories
        }
    )

# Add a new category
def add(request):
    assert isinstance(request, HttpRequest)
    if request.method == 'GET':
        form = CategoryForm
    return render(
        request,
        'app/categories/add.html',
        {
            'form': form
        }
    )
