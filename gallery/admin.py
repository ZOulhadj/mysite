from django.contrib import admin

from .models import *

class AlbumAdmin(admin.ModelAdmin):
    search_fields = ["name"]


class ImageAdmin(admin.ModelAdmin):
    list_display = ["name", "image", "description", "upload_date"]
    search_fields = ["image", "description"]


admin.site.register(Album, AlbumAdmin)
admin.site.register(Image, ImageAdmin)
