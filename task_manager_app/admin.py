from django.contrib import admin
from .models import Task
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Register the Task model in the Django admin panel
admin.site.register(Task)

class CustomUserAdmin(UserAdmin):
    """
    Custom admin panel configuration for the CustomUser model.
    Adds the 'mobile' field to both fieldsets and add_fieldsets.
    """

    # Extend the default UserAdmin fieldsets to include the 'mobile' field
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('mobile',)}),
    )

    # Extend the add_fieldsets to include the 'mobile' field when adding a new user
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('mobile',)}),
    )

# Register the CustomUser model with the custom admin configuration
admin.site.register(CustomUser, CustomUserAdmin)
