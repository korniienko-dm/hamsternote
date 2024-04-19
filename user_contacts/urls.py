from django.contrib import admin
from django.urls import path
from django.urls import include
from django.views.generic.base import TemplateView
from . import views


urlpatterns = [
    path('contacts/', views.contacts_list, name='contacts_list'),
    path('add_contact/', views.add_contact, name='add_contact'),
    path('contacts/<int:contact_id>/', views.contact_detail, name='contact_detail'),
    path('contacts/remove/<int:contact_id>/', views.remove_contact, name='remove_contact'),
]
