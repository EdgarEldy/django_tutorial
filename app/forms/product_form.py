from django.forms import ModelForm
from app.models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fiels = '__all__'