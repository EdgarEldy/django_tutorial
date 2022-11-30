from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.contrib import messages

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


# Save a new category
def store(request):
    assert isinstance(request, HttpRequest)
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
        
        messages.success(request, "Category has been saved successfully !")
            
        return redirect('/categories')

# Edit a category
def edit(request, id):
    assert isinstance(request, HttpRequest)
    if request.method == 'GET':
        if id == 0:
            form = CategoryForm()
        else:
            category = Category.objects.get(pk=id)
            form = CategoryForm(instance=category)
        return render(
            request,
            'app/categories/edit.html',
            {
                'form': form
            }
        )