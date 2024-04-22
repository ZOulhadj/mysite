from django.urls import path, include

from . import views

app_name = "gallery"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("albums/", views.AlbumView.as_view(), name="albums"),
    path("albums/<int:pk>", views.AlbumDetailView.as_view(), name="album_detail")
]
