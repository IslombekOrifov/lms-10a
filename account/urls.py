from django.urls import path

from .views import users_list

app_name = 'account'

urlpatterns = [
    path('users/', users_list, name='users_list'),
]