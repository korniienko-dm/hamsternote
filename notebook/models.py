from django.db import models
from django.contrib.auth.models import User
from users.models import CustomUser


class TimestampMixin(models.Model):
    """
    A mixin class for adding timestamp fields to models.
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def formatted_created_at(self):
        """Formats the creation timestamp into a readable string."""
        return self.created_at.strftime("%d.%m.%Y %H:%M")

    def formatted_updated_at(self):
        """Formats the last update timestamp into a readable string."""
        return self.updated_at.strftime("%d.%m.%Y %H:%M")


class Notebook(TimestampMixin):
    """
    Model class representing a notebook.
    A notebook is a collection of notes created by a user.
    """
    title = models.CharField(max_length=100)
    owner = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='notebooks')
    created_by = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='created_notebooks')

    def __str__(self):
        return self.title
