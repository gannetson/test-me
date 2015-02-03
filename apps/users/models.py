from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    def get_full_name(self):
        return "{0} {1}".format(self.first_name, self.last_name)

    @property
    def full_name(self):
        return self.get_full_name()

