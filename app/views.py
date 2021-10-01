from django.shortcuts import render, redirect
from django.http import HttpRequest
from .forms import *
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from datetime import datetime


# Create your views here.
