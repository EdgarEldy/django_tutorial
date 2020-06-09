"""
Definition of forms.
"""

from django import forms
from .models import Category
from .models import Customer
from .models import Product
from .models import Order

class CategoriesForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class CustomersForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

class ProductsForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class OrdersForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'