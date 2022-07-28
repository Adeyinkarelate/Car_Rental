from dataclasses import field
from django import forms
from .models import Car , Brand
  
class BrandForm(forms.ModelForm):
    class Meta():
        model = Brand
        fields = ('brand_name',)