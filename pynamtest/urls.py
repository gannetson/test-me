from django.conf.urls import patterns, include, url
from django.contrib import admin
from pynamtest.views import HomeView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(), name='home_view'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^users/', include('apps.users.urls')),
    url(r'^tickets/', include('apps.tickets.urls')),
)
