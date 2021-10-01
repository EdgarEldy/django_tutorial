from django.forms import ModelForm
from app.models import *

class ProductsForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'