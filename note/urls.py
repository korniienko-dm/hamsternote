from django.urls import path
from . import views


urlpatterns = [
    path('note/<int:note_id>/', views.note_detail, name='note_detail'),
    path('note_edit/<int:note_id>/', views.note_edit, name='note_edit'),
    path('note_create/<int:notebook_id>/', views.note_create, name='note_create'),
    path('note_delete/<int:note_id>/', views.note_delete, name='note_delete'),
    path('note_delete_from_favorite/<int:note_id>/', views.note_delete_from_favorite, name='note_delete_from_favorite'),
    path('note_add_favorite/<int:note_id>/', views.note_add_favorite, name='note_add_favorite'),
    path('shared_info_note/<int:note_id>/', views.shared_info_note, name='shared_info_note'),
]
