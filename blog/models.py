from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from django.utils.text import slugify

from colorfield.fields import ColorField

class Post(models.Model):
    title = models.CharField(_("title"), max_length=100)
    slug = models.SlugField(unique=True)
    description = models.CharField(_("description"), max_length=200)
    author = models.ForeignKey(
        "core.User",
        on_delete=models.CASCADE,

    )
    created_date = models.DateTimeField(_("created date"), auto_now_add=timezone.now)
    updated_date = models.DateTimeField(_("updated date"), auto_now=timezone.now)
    tags = models.ManyToManyField("tag", blank=False, related_name="posts")
    body = models.TextField(_("body"), max_length=2000, blank=True)
    comments_allows = models.BooleanField(_("comments allowed"), default=True)
    view_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class Tag(models.Model):
    name = models.CharField(_("tag"), max_length=20)
    color = ColorField(default="#ff0000")

    def __str__(self):
        return self.name

class Comment(models.Model):
    user = models.ForeignKey(
        "core.User",
        on_delete=models.CASCADE,
    )
    post = models.ForeignKey(
        "Post",
        on_delete=models.CASCADE,
    )
    created_date = models.DateTimeField(_("created date"), auto_now_add=timezone.now)
    updated_date = models.DateTimeField(_("updated date"), auto_now=timezone.now)
    comment = models.TextField(_("comment"), max_length=500)

    def __str__(self):
        return f"{self.user} on '{self.post}'"
