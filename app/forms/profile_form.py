from django.forms import ModelForm
from app.models import *

class ProfilesForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'