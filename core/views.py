from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group

from .forms import SignUpForm, SignInForm

def index(request):
    return render(request, "core/index.html")

def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=True)

            return redirect("signin")
    else:
        form = SignUpForm()

    return render(request, "core/signup.html", { "form": form })

def signin(request):
    if request.method == "POST":
        form = SignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("/")
    else:
        form = SignInForm()

    return render(request, "core/signin.html", { "form": form })

def signout(request):
    logout(request)

    return redirect("signin")
