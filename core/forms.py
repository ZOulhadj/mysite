from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import User

class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        #fields = UserCreationForm.Meta.fields + ("image",)
        fields = ["username", "password1"]

class LoginForm(AuthenticationForm):
    pass

# class ChangeUserForm(models.Forms):
#     fields = ["username", "image"]
