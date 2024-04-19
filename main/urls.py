from django.urls import path
from main import views


urlpatterns = [
    path('', views.main_page, name='start_page'),
    path('homepage/', views.homepage, name='homepage'),
    # path('accounts/', include('django.contrib.auth.urls')),
]
