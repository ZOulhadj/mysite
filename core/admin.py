from django import forms
from django.core.exceptions import ValidationError
from django.contrib import admin

from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User


class UserAdmin(BaseUserAdmin):
    # Add your custom fields to the fieldsets
    fieldsets = (
        (None, {'fields': ('username', 'password', 'image')}),  # Add 'image' field here
        # Add other fieldsets as needed
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser',
                                    'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    # Customize the list display
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff']



admin.site.register(User, UserAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
admin.site.unregister(Group)
