from django.shortcuts import render, HttpResponseRedirect
from users.forms import UserLoginForm
from django.urls import reverse
from django.contrib import auth
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

    context = {'title': 'GeekShop - Авторизация', 'form': form,}
    return render(request, 'users/login.html', context)


def registration(request):
    context = {'title': 'GeekShop - Регистрация'}
    return render(request, 'users/registration.html', context)
