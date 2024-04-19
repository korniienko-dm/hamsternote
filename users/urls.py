from django.urls import path
from django.urls import include
from registration.views import CustomLoginView


urlpatterns = [
    path("users/login/", CustomLoginView.as_view(), name="login"),
    path('users/', include('django.contrib.auth.urls')),
]
