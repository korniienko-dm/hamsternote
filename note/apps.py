from django.apps import AppConfig

class NoteConfig(AppConfig):
    """
    This class defines the configuration settings for the 'note' app. It specifies the default auto field to use for
    models that do not explicitly define a primary key field, and sets the name of the app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'note'
