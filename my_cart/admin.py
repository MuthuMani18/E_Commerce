from django.contrib import admin
from . models import *


class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'total_price')


admin.site.register(Cart, CartAdmin)


class CartItemsAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product',)


admin.site.register(CartItems, CartItemsAdmin)
