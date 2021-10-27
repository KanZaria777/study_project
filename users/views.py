from django.shortcuts import render, HttpResponseRedirect
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from django.urls import reverse
from django.contrib import auth
from django.contrib import messages

# Функции которые тут написаны господь провозгласил контроллерами

'''
__login__
Первым у нас выполняется блок елс,где создается форма посредством GET и передается снова
После уже когда мы собираемся войти, происходит присваивание данных форме и преедча посредством POST
Далее происходит аутентификация и если она и актив равно Тру, дается разрешение на вход.
На главную мы возвращаемся посредством reverse, можно было бы и просто, но так код более понятен.
form.errors это временная заплатка для чтения ошибок(если таковые есть) в консоли.
'''


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                print(form.errors)
    else:
        form = UserLoginForm()
    context = {'title': 'GeekShop - Авторизация', 'form': form}
    return render(request, 'users/login.html', context)


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Наши поздравления, с успешной регистрацией!')
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegistrationForm()
    context = {'title': 'GeekShop - Регистрация', 'form': form}
    return render(request, 'users/registration.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))

def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(instance=request.user,files=request.FILES, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = UserProfileForm(instance=request.user)
    context = {'title': 'GeekShop - Профиль', 'form': form}
    return render(request, 'users/profile.html', context)
