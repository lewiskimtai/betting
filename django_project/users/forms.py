from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from phonenumber_field.formfields import PhoneNumberField



class UserRegisterForm(UserCreationForm):
    phonenumber = PhoneNumberField()

    class Meta:
        model = User
        fields = ['username', 'phonenumber', 'password1', 'password2']


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    phonenumber = PhoneNumberField()
