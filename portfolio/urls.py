from django.urls import path, include

from . import views

app_name = "portfolio"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<slug:slug>/", views.ProjectDetailView.as_view(), name="project_detail")
]
