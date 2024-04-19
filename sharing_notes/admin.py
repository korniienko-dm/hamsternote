from django.contrib import admin
from .models import SharingNote

@admin.register(SharingNote)
class SharingNoteAdmin(admin.ModelAdmin):
    """
    Admin configuration for the SharingNote model.
    This configuration customizes how SharingNote objects are displayed and filtered in the Django admin interface.
    """
    list_display = ['owner', 'note', 'shared_with', 'can_view', 'can_edit', 'created_at', 'updated_at']
    list_filter = ['owner', 'note', 'shared_with', 'can_view', 'can_edit']
    search_fields = ['owner__username', 'note__title', 'shared_with__user__username']
