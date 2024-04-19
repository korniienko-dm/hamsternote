from django.db import models
from users.models import CustomUser


class Contact(models.Model):
    """
    Model representing a contact relationship between users.
    A contact represents a connection between two users.
    """
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='contacts')
    contact_user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='contact_of')
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['user', 'contact_user']

    def __str__(self):
        return f"{self.contact_user.username}"
