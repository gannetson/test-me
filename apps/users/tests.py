from unittest import skipIf

from django.urls import reverse

from apps.users.models import User
from testme.tests import SeleniumTestCase
from django.test import TestCase
from apps.users.factories import UserFactory
from django.conf import settings


class UserTests(TestCase):

    def test_first_name(self):
        user = UserFactory.create(first_name='Django', last_name='Reinhardt')
        self.assertEqual(user.first_name, 'Django')

    def test_full_name(self):
        user = UserFactory.create(first_name='Django', last_name='Reinhardt')
        self.assertEqual(user.full_name, 'Django Reinhardt')


class UserAdminTests(TestCase):

    def setUp(self):
        super(UserAdminTests, self).setUp()
        self.user_admin_url = reverse('admin:users_user_changelist')
        self.admin_user = UserFactory(is_superuser=True, is_staff=True)

    def test_admin_user_should_login(self):
        response = self.client.get(self.user_admin_url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/admin/login/?next=/admin/users/user/')

    def test_user_admin_has_access(self):
        self.client.force_login(self.admin_user)
        response = self.client.get(self.user_admin_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<h1>Select user to change</h1>')


class LiveUserTests(SeleniumTestCase):

    def setUp(self):
        super(LiveUserTests, self).setUp()
        self.user = UserFactory.create(email='test@example.com')
        self.user.save()

    def visit_page(self, path):
        url = '%s%s' % (self.live_server_url,  path)
        return self.browser.get(url)

    @skipIf(not settings.SELENIUM_TESTS_ENABLED, 'Selenium tests skipped by config.')
    def test_user_list(self):
        self.visit_page('/users/')
        name = self.browser.find_element_by_css_selector('li b')
        email = self.browser.find_element_by_css_selector('li i')
        self.assertEqual(name.text, self.user.get_full_name())
        self.assertEqual(email.text, 'test@example.com')
