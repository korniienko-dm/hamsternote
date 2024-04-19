from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Note the name of your main application (app_hamsternote)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app_hamsternote.settings')

# Create an instance of the Celery class
celery_app = Celery('app_hamsternote')

# Load the Django configuration for the Celery object
celery_app.config_from_object('django.conf:settings', namespace='CELERY')

# Get tasks from Django applications
celery_app.autodiscover_tasks()