from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpRequest
from django.shortcuts import render, redirect

from app.forms import UserForm


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
