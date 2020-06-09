"""
Definition of forms.
"""

from django import forms
from .models import Category
from .models import Customer
from .models import Product

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
