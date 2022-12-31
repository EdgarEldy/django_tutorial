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
from django.urls import path
from app.views import home, categories, products, customers, orders

urlpatterns = [
    path('', home.index, name="home"),
    path('categories/', categories.index, name="categories_index"),
    path('categories/add', categories.add, name="categories_add"),
    path('categories/store', categories.store, name="categories_store"),
    path('categories/edit/<int:id>', categories.edit, name="categories_edit"),
    path('categories/update/<int:id>', categories.update, name="categories_update"),
    path('categories/delete/<int:id>', categories.delete, name="categories_delete"),
    
    # products view
    path('products/', products.index, name="products_index"),
    path('products/add', products.add, name="products_add"),
    path('products/store', products.store, name="products_store"),
    path('products/edit/<int:id>', products.edit, name="products_edit"),
    path('products/update/<int:id>', products.update, name="products_update"),
    path('products/delete/<int:id>', products.delete, name="products_delete"),
    
    # customers view
    path('customers/', customers.index, name="customers_index"),
    path('customers/add', customers.add, name="customers_add"),
    path('customers/store', customers.store, name="customers_store"),
    path('customers/edit/<int:id>', customers.edit, name="customers_edit"),
    path('customers/update/<int:id>', customers.update, name="customers_update"),
    path('customers/delete/<int:id>', customers.delete, name="customers_delete"),
    
    # orders view
    path('orders/', orders.index, name='orders_index'),
    path('orders/add', orders.add, name='orders_add'),

]
