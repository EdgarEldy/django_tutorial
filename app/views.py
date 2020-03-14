from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime


# Create your views here.

def home(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/home/index.html',
        {
            'title': 'Django tutorial'
        }
    )
