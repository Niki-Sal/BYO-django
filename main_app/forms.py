from django import forms
from .models import gardening

class GardeningForm(forms.ModelForm):
    #meta class because that's how django can do it
    class Meta:
        # which model
        model  = gardening
        fields = ['date', 'care']