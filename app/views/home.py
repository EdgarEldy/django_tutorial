# @login_required(login_url='users_login')
from django.http import HttpRequest
from django.shortcuts import render


def home(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/home/index.html'
    )