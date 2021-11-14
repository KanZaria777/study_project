from django.db import models


# модельки это как таблички в бд, только в питоне

class ProductCategory(models.Model):
    name = models.CharField(max_length=64, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=256)
    image = models.ImageField(upload_to='product_images', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} | {self.category.name}'


'''
    Таблица корзины товаров. По идее она должны хранить есть товар в корзине или нет, с помощью
    Булевого типа данных, что оптимально. И ссылаться на товар. Но в идеале, тогда и на пользователя
    Но сейчас наверно рановато. Можно было бы представить скелет, основываясь на опыте SQL
    но тут мы заходим через питон и наверно нет смысла пытаться угадать графы. А user_id сюда врятли впишется:)
    В общем, пока не знаю как сделать кнопку корзины живой. 
'''
'''
class Users(models.Model):
    name = models.CharField(max_length=256)
    e_mail = models.CharField(max_length=256, unique=True)
    #login = models.CharField(max_length=50, unique=True)
    #password = models.CharField(max_length=50) + сюда можно попровать подключить валидаторы django и ключ шифрования
    
class Basket(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    in_the_basket = models.BooleanField(default=0)
'''
