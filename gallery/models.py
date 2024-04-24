from django.db import models
from django.urls import reverse
from django.utils import timezone

class Album(models.Model):
    name = models.CharField(max_length=100)
    cover = models.ImageField(blank=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("gallery:album_detail", args=[self.id])


class Image(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    upload_date = models.DateTimeField(auto_now_add=timezone.now)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, null=True, blank=True)
