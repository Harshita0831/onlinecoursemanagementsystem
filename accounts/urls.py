from django.urls import path
from .views import user_list, register_user

urlpatterns = [
    path('auth/register/', register_user, name='register'),
    path('users/', user_list, name='user-list'),
]