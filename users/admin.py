from django.contrib import admin

from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from registration.forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    """
    This class provides the customization of the Django admin interface for managing
    the custom user model. It specifies the forms used for adding and changing users,
    and customizes the displayed fields in the admin interface.
    """
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username',]


admin.site.register(CustomUser, CustomUserAdmin)
