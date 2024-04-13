
from django.urls import path, include

from . import views

app_name = "blog"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<slug:slug>/", views.PostView.as_view(), name="blog_post")
]
