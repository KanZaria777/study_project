from django.shortcuts import render

from products.models import ProductCategory, Product
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
# функция = контроллер = вьюха

def index(request):
    content = {
        'title': 'GeekShop',
        'title1': 'GeekShop Store'
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


def products(request, category_id=None, page=1):
    content = {'title': 'GeekShop - Каталог', 'categories': ProductCategory.objects.all()}
    if category_id:
        products = Product.objects.filter(category_id=category_id)
    else:
        products = Product.objects.all()
    paginator = Paginator(products, 3)
    try:
        products_paginator = paginator.page(page)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)
    content['products'] = products_paginator
    return render(request, 'products/products.html', content)
