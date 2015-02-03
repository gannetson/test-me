from django.views.generic import DetailView, ListView
from apps.users.models import User


class UserListView(ListView):
    model = User
    template_name = 'users/list.tpl'