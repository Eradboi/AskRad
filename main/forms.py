from django.contrib.auth import login, authenticate
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from captcha.fields import CaptchaField
from .models import *
from django.urls import reverse_lazy
class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    captcha = CaptchaField()
    # the below is for saving the users input into their database the class must be (meta)
    class Meta:
        model = User
        # the fields is to define how the fields of the form would appear
        fields = ["username", "email", "password1", "password2"]


class ChangeForm(forms.Form):
    username = forms.CharField(label='New Username', max_length=150)

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['username', 'comment', 'rating']

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['rating'].widget.attrs['placeholder'] = 'From 1-10'