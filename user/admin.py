from django.contrib import admin
from . import models


class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "email","user_type")
  
    """
    fieldsets = (
      ('User Credentials', {'fields': ('email', 'password')}),
      ('Personal info', {'fields': ('first_name', 'last_name','mobile')}),
     
    )     
"""
    
    search_fields = ('email',)
    ordering = ['id']
    filter_horizontal = ()
admin.site.register(models.User, UserAdmin)
