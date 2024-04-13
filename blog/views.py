from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView

#from django.core.paginator import Paginator

from .models import Post

class IndexView(ListView):
    template_name = "blog/index.html"
    allow_empty = True
    paginate_by = 5

    def get_queryset(self):
        return Post.objects.order_by("-created_date").filter(title__icontains="")


class PostView(DetailView):
    template_name = "blog/post.html"
    model = Post

    def get_object(self):
        obj = super().get_object()
        obj.view_count += 1
        obj.save()
        return obj
