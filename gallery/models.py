from django.db import models
from django.utils import timezone

class Album(models.Model):
    name = models.CharField(max_length=100)
    cover = models.ImageField(blank=False)

    def __str__(self):
        return self.name


class Image(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    upload_date = models.DateTimeField(auto_now_add=timezone.now)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, null=True, blank=True)
