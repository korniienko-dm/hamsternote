from django.db import models
from users.models import CustomUser
from notebook.models import Notebook
from django_ckeditor_5.fields import CKEditor5Field

# Create your models here.


class TimestampMixin(models.Model):
    """
    This mixin class adds 'created_at' and 'updated_at' fields to models. It provides methods to format these timestamp
    fields into readable date and time strings.
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def formatted_created_at(self):
        return self.created_at.strftime("%d.%m.%Y %H:%M")

    def formatted_updated_at(self):
        return self.updated_at.strftime("%d.%m.%Y %H:%M")


class NotePermission(models.TextChoices):
    """
    This class defines choices for the 'permission' field of the Note model. It provides two choices: 'VIEW_ONLY' and
    'EDITABLE', each with a corresponding human-readable label.
    """
    VIEW_ONLY = 'VIEW', 'View Only'
    EDITABLE = 'EDIT', 'Editable'


class Note(TimestampMixin):
    """
    This model represents a note object with fields for 'title', 'content', 'notebook', 'author', 'permission', and
    'favorite'. It inherits from the TimestampMixin to include timestamp fields.
    """
    title = models.CharField(max_length=100)
    content = CKEditor5Field('Content', config_name='extends')
    notebook = models.ForeignKey(
        Notebook, on_delete=models.CASCADE, related_name='notes')
    author = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='created_notes')
    permission = models.CharField(
        max_length=4, choices=NotePermission.choices, default=NotePermission.EDITABLE)
    favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.title
