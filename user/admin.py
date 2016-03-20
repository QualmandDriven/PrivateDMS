from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from user.models import DmsUser

# Register your models here.


class DmsUserInline(admin.StackedInline):
    model = DmsUser
    can_delete = False


class UserAdmin(UserAdmin):
    inlines = [DmsUserInline, ]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
