from django.apps import AppConfig


class UsersConfig(AppConfig):
    """
    AppConfig class for the users app.
    This class represents the configuration for the users app in Django. It specifies
    the default auto field to be used for models and the name of the app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'
