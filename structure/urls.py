from django.urls import path

from .views import(
    academic_year_list, academic_year_delete, academic_year_detail,
    academic_year_update
)

app_name = 'structure'

urlpatterns = [
    path('academic-year/', academic_year_list, name='academic_year_list'),
    path('academic-year/<int:pk>/delete', academic_year_delete, name='academic_year_delete'),
    path('academic-year/<int:id>/detail', academic_year_detail, name='academic_year_detail'),
    path('academic-year/<int:id>/update', academic_year_update, name='academic_year_update'),
]