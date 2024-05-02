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


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    body = forms.CharField(widget=forms.Textarea, max_length=2000)

    def send_email(self):
        print("Sending contact form")
