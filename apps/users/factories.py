import factory
from apps.users.models import User


class UserFactory(factory.DjangoModelFactory):

    class Meta:
        model = User

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')

    email = factory.Faker('email')
    username = factory.Faker('user_name')
    is_active = True
    is_superuser = False
    is_staff = False
