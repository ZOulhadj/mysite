from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

from .models import Album, Image

class IndexView(ListView):
    template_name = "gallery/index.html"
    paginate_by = 20

    def get_queryset(self):
        return Image.objects.order_by("-upload_date")

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data["album_list"] = Album.objects.order_by("name")

        return data


class AlbumView(ListView):
    template_name = "gallery/albums.html"
    model = Album
    pagenate_by = 50


class AlbumDetailView(DetailView):
    template_name = "gallery/album_detail.html"
    model = Album

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data["image_list"] = Image.objects.filter(album=self.object).order_by("-upload_date")

        return data
