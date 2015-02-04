import factory
from apps.users.models import User


class UserFactory(factory.Factory):
    FACTORY_FOR = User

    first_name = factory.Sequence(lambda n: 'John_{0}'.format(n))
    last_name = 'Doe'

    email = factory.Sequence(lambda n: 'john_{0}@doe.org'.format(n))
    username = factory.Sequence(lambda n: 'john_{0}'.format(n))
    is_active = True