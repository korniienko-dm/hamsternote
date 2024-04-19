from django.db import models

from note.models import Note
from users.models import CustomUser


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    remind_at = models.DateTimeField()
    reminder_method = models.CharField(max_length=20, choices=[('email', 'Email')])
    attachment = models.ForeignKey(Note, on_delete=models.CASCADE, null=True, blank=True)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
