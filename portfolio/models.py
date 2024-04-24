from django.db import models
from django.urls import reverse
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
    category = models.ManyToManyField("category", blank=True, related_name="projects")
    created_date = models.DateTimeField(auto_now_add=timezone.now)
    updated_date = models.DateTimeField(auto_now=timezone.now)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


    def get_absolute_url(self):
        return reverse("portfolio:project_detail", args=[self.slug])


class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=100, blank=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


class School(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(blank=True, upload_to="images/portfolio/education")
    website = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name


class WorkPlace(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(blank=True, upload_to="images/portfolio/work")
    website = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name


class Education(models.Model):
    school = models.ForeignKey(
        School,
        on_delete=models.CASCADE,
        null=True,
        blank=False
    )
    start_date = models.DateField()
    end_date = models.DateField()
    grade = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.school.name


class Work(models.Model):
    work_place = models.ForeignKey(
        WorkPlace,
        on_delete=models.CASCADE,
        null=True,
        blank=False
    )
    job_title = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    text = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.work_place.name


class Achievement(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    date_of_award = models.DateField()

    def __str__(self):
        return self.name
