from django.contrib import admin
from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """
    Admin view for managing contacts.
    """
    list_display = ('user', 'contact_user', 'added_at')
    list_filter = ('added_at',)
