from django.shortcuts import render
from django.http import HttpRequest


# Create your views here.

def home(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/home/index.html'
    )
