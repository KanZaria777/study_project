from django.shortcuts import render

from products.models import ProductCategory, Product
# Create your views here.
# функция = контроллер = вьюха

def index(request):
    content = {
        'title': 'GeekShop'
    }
    return render(request, 'products/index.html', content)


'''
    Сначала я подумал почему бы не использовать list_products, чтобы было понятнее
    А то products получается вложенным и это сейчас немного сложно.
    А потом понял, что при наполнении динамическим контентом, куда понятнее обращаться
    к products, нежели list_products. Все проще, если забыть о имени контроллера.
    Главное помнить, что мы обращаемся к ключу, а не к функции. И с одинаковыми именами
    есть шанс запутаться и неверно истолковать по началу для себя.    
'''
def products(request):
    content = {
        'title': 'GeekShop - Каталог',
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all(),
    }
    return render(request, 'products/products.html', content)




