from unicodedata import category
from django.contrib import admin
from .models import Product

# @admin.register(Category)


class ProductAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'user_id', 'category', 'price')


admin.site.register(Product, ProductAdmin)
# admin.site.register(Category)
