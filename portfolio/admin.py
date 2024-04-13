from django.contrib import admin

from .models import *

class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    readonly_fields = ["created_date", "updated_date"]

admin.site.register(Project, ProjectAdmin)
