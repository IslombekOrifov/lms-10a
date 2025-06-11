from django.shortcuts import render, redirect

from .models import AcademicYear, Kafedra
from .forms import AcademicYearForm, KafedraForm


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

def academic_year_update(request, id):
    academic_year = AcademicYear.objects.get(pk=id)
    if request.method == 'POST':
        form = AcademicYearForm(request.POST, instance=academic_year)
        if form.is_valid():
            form.save()
            return redirect('structure:academic_year_list')
    else:
        form = AcademicYearForm(instance=academic_year)
    return render(request, 'structure/academ-update.html', {'form': form})


def academic_year_create(request):
    if request.method == 'POST':
        form = AcademicYearForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('structure:academic_year_list')
    else:
        form = AcademicYearForm()
    return render(request, 'structure/academ-update.html', {'form': form})



def kafedra_list(request):
    kafedras = Kafedra.objects.all()
    context = {
        'kafedras': kafedras
    }
    return render(request, 'structure/kafedra.html', context)

def kafedra_delete(request, pk):
    kafedras = Kafedra.objects.get(id=pk).delete()
    return redirect('structure:kafedra_list')

def kafedra_detail(request, id):
    kafedra = Kafedra.objects.get(pk=id)
    context = {
        'kafedra': kafedra
    }
    return render(request, 'structure/kafedra-detail.html', context)

def kafedra_update(request, id):
    kafedra = Kafedra.objects.get(pk=id)
    if request.method == 'POST':
        form = KafedraForm(request.POST, instance=kafedra)
        if form.is_valid():
            form.save()
            return redirect('structure:kafedra_list')
    else:
        form = KafedraForm(instance=kafedra)
    return render(request, 'structure/kafedra-update.html', {'form': form})

def kafedra_create(request):
    if request.method == 'POST':
        form = KafedraForm(request.POST)
        if form.is_valid():
            kafedra = form.save(commit=False)
            kafedra.school = request.user.school
            kafedra.save()
            return redirect('structure:kafedra_list')
    else:
        form = KafedraForm()
    return render(request, 'structure/kafedra-update.html', {'form': form})