from django.shortcuts import render, redirect
from django.http import Http404

from .models import School
from .forms import SchoolForm


def dashboard(request):
    return render(request, 'main/index.html')


def school_detail(request):
    user = request.user
    school = user.school
    if school and user.role.name == 'director':
        print('keldi')
        if request.method == 'POST':
            form = SchoolForm(request.POST, instance=school)
            if form.is_valid():
                form.save()
                return redirect('main:school_detail')
        else:
            form = SchoolForm(instance=school)
        return render(request, 'main/company.html', {'form': form})
    else:
        raise Http404()