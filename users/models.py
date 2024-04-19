from django.db import models

from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """
    Custom user model extending Django's AbstractUser.
    This model represents a custom user in the application, extending Django's
    AbstractUser model. It adds an email field, which is unique.
    """
    email = models.EmailField(unique=True)

    def __str__(self):
        return f'{self.username} ({self.email})'
