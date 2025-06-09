from django.shortcuts import render, redirect

from .models import AcademicYear


def academic_year_list(request):
    academic_years = AcademicYear.objects.all()
    context = {
        'academic_years': academic_years
    }
    return render(request, 'structure/academic-year.html', context)


def academic_year_delete(request, pk):
    academic_years = AcademicYear.objects.get(id=pk).delete()
    return redirect('structure:academic_year_list')

def academic_year_detail(request, id):
    academic_year = AcademicYear.objects.get(pk=id)
    context = {
        'academic_year': academic_year
    }
    return render(request, 'structure/academ-detail.html', context)