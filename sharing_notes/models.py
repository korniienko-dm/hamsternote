from django.db import models
from users.models import CustomUser
from note.models import Note
from user_contacts.models import Contact


class TimestampMixin(models.Model):
    """
    A mixin class to provide timestamp fields for models.
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def formatted_created_at(self):
        """Format the creation timestamp."""
        return self.created_at.strftime("%d.%m.%Y %H:%M")

    def formatted_updated_at(self):
        """Format the last update timestamp."""
        return self.updated_at.strftime("%d.%m.%Y %H:%M")


class SharingNote(TimestampMixin):
    """
    Model class representing sharing notes.
    This model represents notes shared by users with other users.
    """
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    note = models.ForeignKey(Note, on_delete=models.CASCADE)
    shared_with = models.ForeignKey(Contact, on_delete=models.CASCADE)
    can_view = models.BooleanField(default=True)
    can_edit = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.note.title}"
