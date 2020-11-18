from django.contrib import admin

from products.models.product import Product
from products.models.category import Category
from products.models.tag import Tag

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Tag)