from django.contrib import admin
from apps.users.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name')
    readonly_fields = ('last_login', 'date_joined')
    fields = ('username', 'email', 'first_name', 'last_name',
              'is_active', 'is_superuser', 'is_staff') + readonly_fields

admin.site.register(User, UserAdmin)