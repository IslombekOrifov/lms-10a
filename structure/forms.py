from django import forms
from django.db.models import Q

from .models import AcademicYear



class AcademicYearForm(forms.ModelForm):
    class Meta:
        model = AcademicYear
        fields = ['name', 'season', 'start_date', 'end_date', 'is_active', 'parent']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'name': 'Academic Year Name',
            'season': 'Season',
            'start_date': 'Start Date',
            'end_date': 'End Date',
        }
    def __init__(self, *args, instance=None, **kwargs):
        super().__init__(*args, **kwargs)
        if instance:
            self.fields['parent'].queryset = AcademicYear.objects.exclude(Q(pk=instance.pk) | Q(parent=instance))     