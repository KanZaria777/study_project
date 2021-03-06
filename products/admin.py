from django.contrib import admin

from products.models import ProductCategory, Product

admin.site.register(ProductCategory)
#admin.site.register(Product)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category')
    fields = ('name', 'image', 'description', 'price', 'quantity', 'category')
    search_fields = ('name',)
