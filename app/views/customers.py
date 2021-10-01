from django.http import HttpRequest
from django.shortcuts import render, redirect
from app.models import Customer
from app.forms import CustomersForm


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