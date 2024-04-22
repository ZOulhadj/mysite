from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    image = models.ImageField(_('image'), upload_to="images/", default="images/default_image.jpg")

class Social(models.Model):
    name = models.CharField(max_length=20)
    website = models.URLField(max_length=100, blank=False)

    def __str__(self):
        return self.name
