from django.contrib import admin

from .models import *

class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    readonly_fields = ["created_date", "updated_date"]
    filter_horizontal = ("category",)


class SchoolAdmin(admin.ModelAdmin):
    search_fields = ["name"]


class WorkPlaceAdmin(admin.ModelAdmin):
    search_fields = ["name"]


class EducationAdmin(admin.ModelAdmin):
    list_display = ["school", "grade", "start_date", "end_date"]
    search_fields = ["school", "grade"]
    ordering = ["-start_date"]


class WorkAdmin(admin.ModelAdmin):
    list_display = ["job_title", "start_date", "end_date"]
    search_fields = ["job_title"]


class AchievementAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "date_of_award"]
    search_fields = ["name"]


admin.site.register(Project, ProjectAdmin)
admin.site.register(Category)
admin.site.register(School, SchoolAdmin)
admin.site.register(WorkPlace, WorkPlaceAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(Work, WorkAdmin)
admin.site.register(Achievement, AchievementAdmin)
