from django.contrib import admin
from order.models import Orders, OrderedItems


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'payment_options')


admin.site.register(Orders, OrderAdmin)


class OrderItemsAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'order')


admin.site.register(OrderedItems, OrderItemsAdmin)
