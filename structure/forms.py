from django import forms
from django.db.models import Q

from .models import AcademicYear, Kafedra
from account.models import CustomUser



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
            
            
class KafedraForm(forms.ModelForm):
    class Meta:
        model = Kafedra
        fields = ['name', 'code', 'is_active', 'department_user',]

    def __init__(self, *args, instance=None, **kwargs):
        super().__init__(*args, **kwargs)
        if instance:
            self.fields['department_user'].queryset = CustomUser.objects.exclude(Q(is_worker=False) | Q(role__name__in=['director', 'student', 'stylist', 'tutor', 'accountant']) | ~Q(company=self.request.user.company))     