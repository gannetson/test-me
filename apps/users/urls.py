from django.conf.urls import patterns, url
from apps.users.views import UserListView

urlpatterns = patterns('',
    url(r'^$', UserListView.as_view(), name='user_list'),
)
