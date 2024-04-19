from django.urls import path
from . import views

urlpatterns = [
    path('shared_note_list/', views.shared_note_list, name='shared_note_list'),
    path('shared_note_from_me/', views.shared_note_from_me, name='shared_note_from_me'),
    path('shared_note_from_me_detail/<int:shared_note_id>/', views.shared_note_from_me_detail, name='shared_note_from_me_detail'),
    path('shared_note_from_me_edit/<int:shared_note_id>/', views.shared_note_from_me_edit, name='shared_note_from_me_edit'),
    path('shared_note_from_me_settings_change/<int:shared_note_id>/', views.shared_note_from_me_settings_change, name='shared_note_from_me_settings_change'),
    path('shared_note_for_me/', views.shared_note_for_me, name='shared_note_for_me'),
    path('shared_note_for_me_detail/<int:shared_note_id>/', views.shared_note_for_me_detail, name='shared_note_for_me_detail'),
    path('shared_note_for_me_edit/<int:shared_note_id>/', views.shared_note_for_me_edit, name='shared_note_for_me_edit'),
    path('change_access_view_rights/<int:note_shared_id>/', views.change_access_view_rights, name='change_access_view_rights'),
    path('change_access_edit_rights/<int:note_shared_id>/', views.change_access_edit_rights, name='change_access_edit_rights'),
    path('del_contact_from_shared_note/<int:note_shared_id>/', views.del_contact_from_shared_note, name='del_contact_from_shared_note'),
]