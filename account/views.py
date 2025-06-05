from django.shortcuts import render

from .models import CustomUser, Role, RoleName


def users_list(request):
    users = CustomUser.objects.filter(role__name=RoleName.STUDENT)
    context = {
        'users': users,
    }
    return render(request, 'account/users-list.html', context)