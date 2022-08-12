
from dataclasses import field
from django import forms
from .models import Car , Brand  , Booking
  
class BrandForm(forms.ModelForm):
    class Meta():
        model = Brand
        fields = ('brand_name',)
        
class BookingForm(forms.ModelForm):
    class Meta():
        model = Booking
        fields = ( 'city','to_state','To_agree')