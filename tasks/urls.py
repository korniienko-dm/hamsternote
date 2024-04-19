# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('create_task/', views.create_task, name='create_task'),
    path('tasks_list/', views.tasks_list, name='tasks_list'),
]