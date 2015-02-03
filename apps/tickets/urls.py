from django.conf.urls import patterns, url
from apps.tickets.views import TicketListView

urlpatterns = patterns('',
    url(r'^$', TicketListView.as_view(), name='ticket_list'),
)