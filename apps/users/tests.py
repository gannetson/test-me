from unittest import skipIf

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
