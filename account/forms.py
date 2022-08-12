from dataclasses import field
from typing import Any
from django import forms 
from .models import User 
from django.contrib.auth.forms import UserCreationForm

class ProfileForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ('first_name', 'username' , 'email' , 'password1','password2' , 'phone_number' , 'profile_image' , )
        
        
    def __init__(self, *args: Any, **kwargs: Any) -> None:
          super(ProfileForm , self).__init__(*args, **kwargs)
          
          for fieldname in ( 'username' , 'email' , 'password1','password2' , 'phone_number' , 'profile_image' , ):
            self.fields[fieldname].help_text = None
            
            
# Editprofile
class EditProfileForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ( 'first_name','last_name','username' , 'email' ,  'phone_number' , 'profile_image' , )
        
        
    def __init__(self, *args: Any, **kwargs: Any) -> None:
          super(EditProfileForm , self).__init__(*args, **kwargs)
          
          for fieldname in ( 'first_name','last_name','username' , 'email' ,  'phone_number' , 'profile_image' , ):
            self.fields[fieldname].help_text = None