from django.apps import AppConfig


class NotebookConfig(AppConfig):
    """
    This class represents the configuration for the 'notebook' app. It specifies the default auto field to use
    for models in the app and the name of the app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'notebook'
