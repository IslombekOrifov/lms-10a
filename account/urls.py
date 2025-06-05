from django.urls import path

from .views import users_list, user_detail, user_delete

app_name = 'account'

urlpatterns = [
    path('users/', users_list, name='users_list'),
    path('users/<int:user_id>/', user_detail, name='user_detail'),
    path('users/delete/<int:user_id>/', user_delete, name='user_delete'),
]