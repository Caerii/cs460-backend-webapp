from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import User_Data


# Register your models here.

class User_DataInline(admin.StackedInline):
    model = User_Data
    can_delete = True
    verbose_name_plural = "User Type"

class UserAdmin(BaseUserAdmin):
    inlines = [User_DataInline]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
