from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django import forms
from .models import *

class RegisterForm(UserCreationForm):
	email = forms.EmailField(required=True)
	class Meta:
		model = get_user_model()
		fields = ('username', 'email', 'password1', 'password2')

class LoginForm(AuthenticationForm):
	username = forms.CharField(label='Email')

class BookForm(forms.ModelForm):
    class Meta:
        model= Book
        fields=['name','author','category']