from django.contrib import admin
from apps.users.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name')


admin.site.register(User, UserAdmin)