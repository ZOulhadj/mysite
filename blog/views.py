from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView

from .models import Post, Tag

class IndexView(ListView):
    template_name = "blog/index.html"
    allow_empty = True
    paginate_by = 20

    def get_queryset(self):
        return Post.objects.order_by("-created_date").filter(title__icontains="")

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data["tag_list"] = Tag.objects.order_by("name")

        return data


class PostView(DetailView):
    template_name = "blog/post.html"
    model = Post

    def get_object(self):
        obj = super().get_object()
        obj.view_count += 1
        obj.save()
        return obj

class TagDetailView(DetailView):
    template_name = "blog/tag_posts.html"
    model = Tag

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data["post_list"] = Post.objects.filter(tags=self.object)

        return data
