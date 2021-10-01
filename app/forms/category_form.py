from django.forms import ModelForm
from app.models import *

class CategoriesForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'