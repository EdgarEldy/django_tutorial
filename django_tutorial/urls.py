"""django_tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.urls import path

import app.forms
import app.views

urlpatterns = [
   # path('admin/', admin.site.urls),
     url(r'^$', app.views.home, name='home'),
     url(r'^categories/$', app.views.categories_index, name='categories_index'),
     url(r'^categories/add$', app.views.categories_add, name='categories_add'),
     path('categories/edit/<int:id>', app.views.categories_edit, name='categories_edit'),
     path('categories/delete/<int:id>', app.views.categories_delete, name='categories_delete'),

     path('customers', app.views.customers_index, name='customers_index'),
     path('customers/add', app.views.customers_add, name='customers_add'),
     path('customers/edit/<int:id>', app.views.customers_edit, name='customers_edit'),
     path('customers/delete/<int:id>', app.views.customers_delete, name='customers_delete'),

     path('products',app.views.products_index, name='products_index'),
     path('products/add', app.views.products_add, name='products_add'),
     path('products/edit/<int:id>', app.views.products_edit, name='products_edit'),
     path('products/delete/<int:id>', app.views.products_delete, name='products_delete'),

     path('orders',app.views.orders_index, name='orders_index'),
     path('orders/add', app.views.orders_add, name='orders_add'),
     path('orders/edit/<int:id>', app.views.orders_edit, name='orders_edit'),
     path('orders/delete/<int:id>', app.views.orders_delete, name='orders_delete'),
]
