from django.urls import path, include

from . import views

app_name = "blog"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("post/<slug:slug>/", views.PostView.as_view(), name="post"),
    path("tag/<int:pk>/", views.TagDetailView.as_view(), name="tag"),
    #path("feed/", views.PostFeed(), name="feed")
]
