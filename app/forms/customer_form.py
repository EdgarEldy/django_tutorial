from django.forms import ModelForm
from app.models import *

class CustomersForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'