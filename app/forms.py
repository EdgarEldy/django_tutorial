"""
Definition of forms.
"""

from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['product'].queryset = Product.objects.none()

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']