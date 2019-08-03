from django.conf.urls import include, url
from django.contrib import admin

from .views import HomeView

admin.autodiscover()

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home_view'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^users/', include('apps.users.urls')),
    url(r'^tickets/', include('apps.tickets.urls')),
]
