from django.shortcuts import render

# Create your views here.
# функция = контроллер = вьюха

def index(request):
    return render(request, 'products/index.html')

def products(request):
    return render(request, 'products/products.html')




