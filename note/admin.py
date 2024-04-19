from django.contrib import admin
from .models import Note
from django_ckeditor_5.widgets import CKEditor5Widget
from django.db import models


# Register your models here.
class NoteAdmin(admin.ModelAdmin):
    """
    Custom admin class for the Note model.

    This class defines the display, search, and filter options for the Note model in the Django admin interface.

    Attributes:
        list_display (tuple): Tuple containing the fields to display in the list view of the admin interface.
        search_fields (tuple): Tuple containing the fields to enable search functionality in the admin interface.
        list_filter (tuple): Tuple containing the fields to enable filtering functionality in the admin interface.
        formfield_overrides (dict): Dictionary containing form field overrides, particularly for text fields using
        CKEditor5Widget for rich text editing.
    """
    list_display = ('title', 'notebook', 'author', 'created_at', 'updated_at')
    search_fields = ('title', 'content')
    list_filter = ('notebook', 'author', 'created_at', 'updated_at')
    formfield_overrides = {
        models.TextField: {'widget': CKEditor5Widget}
    }

admin.site.register(Note, NoteAdmin)
