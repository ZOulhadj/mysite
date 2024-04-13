from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Project

class IndexView(ListView):
    template_name = "portfolio/index.html"
    model = Project

class ProjectDetailView(DetailView):
    template_name = "portfolio/detail.html"
    model = Project
