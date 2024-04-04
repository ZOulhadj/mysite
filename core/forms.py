from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User

class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        #fields = UserCreationForm.Meta.fields + ("custom_field",)
        fields = UserCreationForm.Meta.fields
