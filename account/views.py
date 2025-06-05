from django.shortcuts import render, redirect
from django.http import Http404

from .models import CustomUser, Role, RoleName


def users_list(request):
    users = CustomUser.objects.filter(role__name=RoleName.STUDENT)
    context = {
        'users': users,
    }
    return render(request, 'account/users-list.html', context)


def user_detail(request, user_id):
    user = CustomUser.objects.get(id=user_id)
    context = {
        'user': user,
    }
    return render(request, 'account/user-detail.html', context)


def user_delete(request, user_id):
    user = CustomUser.objects.get(id=user_id)
    if request.method == 'POST':
        user.delete()
        return redirect('account:users_list')   
    raise Http404("User not found")