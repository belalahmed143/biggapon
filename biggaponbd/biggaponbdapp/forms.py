from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegistrationForm(UserCreationForm):
    first_name =forms.CharField(max_length=20)
    last_name =forms.CharField(max_length=20)
    email =forms.EmailField()
    
    class Meta:
        model =User
        fields =['first_name', 'last_name', 'username', 'email', 'password1','password2']

class UserUpdateform(forms.ModelForm):
    first_name =forms.CharField(max_length=20)
    last_name =forms.CharField(max_length=20)
    email =forms.EmailField()

    class Meta:
        model =User
        fields =['first_name', 'last_name', 'username', 'email']

class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model =Profile
        fields =['profileImg']

        
