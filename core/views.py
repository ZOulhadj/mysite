from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from django.views.generic.base import TemplateView
from django.views.generic import CreateView
from django.views.generic.edit import FormView

from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Social
from .forms import ContactForm, SignUpForm, LoginForm

from blog.models import Post

class IndexView(TemplateView):
    template_name = "core/index.html"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data["social_list"] = Social.objects.order_by("name")
        data["post_list"] = Post.objects.filter(published=True).order_by("-created_date")[:5]

        return data


class ContactView(FormView):
    template_name = "core/contact.html"
    form_class = ContactForm
    success_url = "/thanks/"

    def form_valid(self, form):
        form.send_email()

        return super().form_valid(form)


# @TODO: Redirect if already signed in
class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy("login")
    template_name = "core/signup.html"

class LoginView(auth_views.LoginView):
    template_name = "core/login.html"
    authentication_form = LoginForm
    next_page = "/"
    redirect_authenticated_user = True

class LogoutView(auth_views.LogoutView):
    template_name = "core/logout.html"
    next_page = "/"

class PasswordChangeView(auth_views.PasswordChangeView):
    #template_name = "core/password_change_form.html"
    pass

class PasswordChangeDoneView(auth_views.PasswordChangeDoneView):
    #template_name = "core/password_change_done.html"
    pass

class PasswordResetView(auth_views.PasswordResetView):
    #template_name = "core/password_reset_form.html"
    pass

class PasswordResetDoneView(auth_views.PasswordResetDoneView):
    #template_name = "core/password_reset_done.html"
    pass

class PasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    #template_name = "core/password_reset_confirm.html"
    pass

class PasswordResetCompleteView(auth_views.PasswordResetCompleteView):
    #template_name = "core/password_reset_complete.html"
    pass

class ProfileView(LoginRequiredMixin, TemplateView):
    login_url = "/login"
    redirect_field_name = "redirect_to"
    template_name = "core/profile.html"
