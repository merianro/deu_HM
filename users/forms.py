from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class RegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2', 'full_name', 'date_of_birth', 'phone_number', 'address', 'gender', 'profile_picture')