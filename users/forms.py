from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django import forms
 
class CreateUserForm(UserCreationForm):
      email= forms.EmailField(help_text='Required')
      class Meta:
        model= User
        fields=['username','email','password1','password2']

class CheckUserForm(AuthenticationForm):
      email= forms.EmailField(help_text='Required')
      class Meta:
        model= User
        fields=['email','password','username']