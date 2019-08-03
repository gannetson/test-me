from django.conf.urls import url

from apps.tickets.views import TicketListView

urlpatterns = [
    url(r'^$', TicketListView.as_view(), name='ticket_list'),
]