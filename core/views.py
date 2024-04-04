from django.http import HttpResponse
from django.shortcuts import render, redirect

from django.views.generic.base import TemplateView

from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin

class IndexView(TemplateView):
    template_name = "core/index.html"

class LoginView(auth_views.LoginView):
    template_name = "core/login.html"
    next_page = "profile"

class LogoutView(auth_views.LogoutView):
    template_name = "core/logout.html"

class PasswordChangeView(auth_views.PasswordChangeView):
    template_name = "core/password_change_form.html"

class PasswordChangeDoneView(auth_views.PasswordChangeDoneView):
    template_name = "core/password_change_done.html"

class PasswordResetView(auth_views.PasswordResetView):
    template_name = "core/password_reset_form.html"

class PasswordResetDoneView(auth_views.PasswordResetDoneView):
    template_name = "core/password_reset_done.html"

class PasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    template_name = "core/password_reset_confirm.html"

class PasswordResetCompleteView(auth_views.PasswordResetCompleteView):
    template_name = "core/password_reset_complete.html"

class ProfileView(LoginRequiredMixin, TemplateView):
    login_url = "/login"
    redirect_field_name = "redirect_to"

    template_name = "core/profile.html"
