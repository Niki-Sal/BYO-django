from django import forms
from .models import Gardening

class GardeningForm(forms.ModelForm):
    #meta class because that's how django can do it
    class Meta:
        # which model
        model  = Gardening
        fields = ['date', 'care']