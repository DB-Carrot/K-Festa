from django import forms
from .models import User

class UserSignupForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = {'user_id', 'password', 'name','address', 'phone' }



class UserLoginForm(forms.ModelForm):

    class Meta:
        model = User
        fields = {'user_id', 'password'}