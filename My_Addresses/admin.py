from django.contrib import admin
from . models import Address


class AddressAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'user_id')


admin.site.register(Address, AddressAdmin)
