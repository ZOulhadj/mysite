from django.contrib.syndication.views import Feed

from .models import Post

class BlogPostFeed(Feed):
    title = "Blog posts"
    link = "/rss/"
    description = "Latest 5 blog posts via RSS"

    def items(self):
        return Post.objects.order_by("-created_date")[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.description
