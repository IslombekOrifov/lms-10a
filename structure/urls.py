from django.urls import path

from .views import academic_year_list

app_name = 'structure'

urlpatterns = [
    path('academic-year/', academic_year_list, name='academic_year_list'),
]