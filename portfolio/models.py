from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from django.utils.text import slugify

class Project(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    version_control = models.URLField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    text = models.TextField(max_length=2000, blank=True)
    featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=timezone.now)
    updated_date = models.DateTimeField(auto_now=timezone.now)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
