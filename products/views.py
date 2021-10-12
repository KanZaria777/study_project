from django.shortcuts import render

# Create your views here.
# функция = контроллер = вьюха

def index(request):
    content = {
        'title': 'GeekShop',
        'name': 'GeekShop Store'
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
        'title': 'GeekShop',
        'products': [
            {'name': 'Худи черного цвета с монограммами adidas Originals', 'price': '6 090,00',
             'description': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.',
             'picture': 'Adidas-hoodie.png'},
            {'name': 'Синяя куртка The North Face', 'price': '23 725,00',
             'description': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.',
             'picture': 'Blue-jacket-The-North-Face.png'},
            {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN', 'price': '3 390,00',
             'description': 'Материал с плюшевой текстурой. Удобный и мягкий.',
             'picture': 'Brown-sports-oversized-top-ASOS-DESIGN.png'},
            {'name': 'Черный рюкзак Nike Heritage', 'price': '2 340,00',
             'description': 'Плотная ткань. Легкий материал.',
             'picture': 'Black-Nike-Heritage-backpack.png'},
            {'name': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex', 'price': '13 590,00',
             'description': 'Гладкий кожаный верх. Натуральный материал.',
             'picture': 'Black-Dr-Martens-shoes.png'},
            {'name': 'Темно-синие широкие строгие брюки ASOS DESIGN', 'price': '2 890,00',
             'description': 'Легкая эластичная ткань сирсакер Фактурная ткань.',
             'picture': 'Dark-blue-wide-leg-ASOs-DESIGN-trousers.png'}
        ],
        'send_to_cart': 'Отправить в корзину'
    }
    return render(request, 'products/products.html', content)




