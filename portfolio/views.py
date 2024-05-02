from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView

from .models import Project, Education, Work, Achievement

class IndexView(ListView):
    template_name = "portfolio/index.html"
    model = Project

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data["featured_list"] = Project.objects.filter(featured=True)

        return data


class ProjectDetailView(DetailView):
    template_name = "portfolio/detail.html"
    model = Project


class CVView(TemplateView):
    template_name = "portfolio/cv.html"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data["education_list"] = Education.objects.order_by("-start_date")
        data["work_list"] = Work.objects.order_by("-start_date")
        data["achievement_list"] = Achievement.objects.order_by("-date_of_award")

        return data
