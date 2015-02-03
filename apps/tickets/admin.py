from django.contrib import admin
from apps.tickets.models import Ticket
from apps.users.models import User


class TicketAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')


admin.site.register(Ticket, TicketAdmin)