from django.http import HttpRequest
from django.shortcuts import render, redirect
from app.models import *
from app.forms import *


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
