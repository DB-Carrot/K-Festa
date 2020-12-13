from django.contrib import admin
from account.models import *
# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'name', 'address', 'phone']
    search_filds = ['user_id']
