from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView
from django.contrib.syndication.views import Feed
from django.db.models import Q

from .models import Post, Tag

from .forms import SearchForm

class IndexView(ListView):
    template_name = "blog/index.html"
    allow_empty = True
    paginate_by = 20

    def get_queryset(self):
        query = self.request.GET.get("s")
        if query == None:
            query = ""

        return Post.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query),
            published=True).order_by("-created_date")

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data["tag_list"] = Tag.objects.order_by("name")
        data["form"] = SearchForm()


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
        data["post_list"] = Post.objects.filter(tags=self.object, published=True).order_by("-created_date")

        return data


class PostFeed(Feed):
    title = "Blog posts"
    description_template = "blog/index.html"

    def get_object(self, request, post_id):
        return Post.objects.get(pk=post_id)

    def link(self, obj):
        return obj.get_absolute_url()

    def items(self):
        return Post.objects.all()

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.description
