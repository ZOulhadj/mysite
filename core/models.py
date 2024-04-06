from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    image = models.ImageField(_('image'), upload_to="images/", default="images/default_image.jpg")

class Tag(models.Model):
    name = models.CharField(_("tag"), max_length=20)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(_("title"), max_length=100)
    description = models.CharField(_("description"), max_length=200)
    author = models.ForeignKey(
        "User",
        on_delete=models.CASCADE,
    )
    tags = models.ManyToManyField("tag")

    def __str__(self):
        return self.title

class Comment(models.Model):
    author = models.ForeignKey(
        "User",
        on_delete=models.CASCADE,
    )
    post = models.ForeignKey(
        "Post",
        on_delete=models.CASCADE,
    )

    text = models.TextField(_("text"), max_length=500)
