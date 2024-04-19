from django.urls import path
from . import views


urlpatterns = [
    path('notebooks/', views.notebook_list, name='notebook_list'),
    path('notebooks/notebook/<int:notebook_id>/', views.notebook_detail, name='notebook_detail'),
    path('notebooks/notebook_create/', views.notebook_create, name='notebook_create'),
    path('notebooks/notebook_delete/<int:notebook_id>/', views.notebook_delete, name='notebook_delete'),
    path('notebooks/notebook_edit/<int:notebook_id>/', views.notebook_edit, name='notebook_edit'),
]
