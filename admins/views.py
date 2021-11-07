from django.shortcuts import render, HttpResponseRedirect
from users.models import User
from admins.forms import UserAdminRegistrationForm, UserAdminProfileForm
from django.urls import reverse
from django.contrib.auth.decorators import user_passes_test


@user_passes_test(lambda u: u.is_staff)
def index(request):
    context = {'title': 'GeekShop - Админ Панель'}
    return render(request, 'admins/index.html', context)


def admin_users_create(request):
    if request.method == 'POST':
        form = UserAdminRegistrationForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_users'))
    else:
        form = UserAdminRegistrationForm()
    context = {'title': 'GeekShop - Создание пользователя', 'form': form}
    return render(request, 'admins/admin-users-create.html', context)


def admin_users(request):
    context = {
        'title': 'GeekShop - Пользователи',
        'users': User.objects.all(),
    }
    return render(request, 'admins/admin-users-read.html', context)


def admin_users_update(request, id):
    selected_user = User.objects.get(id=id)
    if request.method == 'POST':
        form = UserAdminProfileForm(instance=selected_user, files=request.FILES, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_users'))
    else:
        form = UserAdminProfileForm(instance=selected_user)
    context = {'title': 'GeekShop - Обновление пользователей',
               'form': form,
               'selected_user': selected_user,
               }
    return render(request, 'admins/admin-users-update-delete.html', context)


# не просто контроллер, а обработчик события
def admin_users_delete(request, id):
    user = User.objects.get(id=id)
    user.safe_delete()  # вынесли часть логики в модели, разгрузили контроллер с перспективой
    return HttpResponseRedirect(reverse('admins:admin_users'))
