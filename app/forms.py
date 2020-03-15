"""
Definition of forms.
"""

from django import forms
from .models import Category

class CategoriesForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        # cat_name = forms.CharField(max_length=254,
        #                            widget=forms.TextInput({
        #                                'class': 'form-control',
        #                                'placeholder':'Category name'
        #                            }))