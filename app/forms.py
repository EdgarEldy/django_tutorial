"""
Definition of forms.
"""

from django.forms import ModelForm
from .models import Category
from .models import Customer
from .models import Product
from .models import Order

class CategoriesForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class CustomersForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

class ProductsForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class OrdersForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'