from django.contrib import admin

from .models import *

class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "description", "author", "created_date", "updated_date"]
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ["view_count", "created_date", "updated_date"]
    filter_horizontal = ("tags",)
    search_fields = ["title", "tags__name"]

class TagAdmin(admin.ModelAdmin):
    search_fields = ["name"]

class CommentAdmin(admin.ModelAdmin):
    #list_display = ["user", "comment", "created_date", "updated_date"]
    pass

admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
