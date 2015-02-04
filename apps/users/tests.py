from pynamtest.tests import SeleniumTestCase
from django.test import TestCase
from django.utils.unittest.case import skipIf
from apps.users.factories import UserFactory
from apps.users.models import User
from selenium import webdriver
from django.conf import settings


class UserTests(TestCase):

    def test_full_name(self):
        user = UserFactory.create(first_name='Django', last_name='Reinhardt')
        self.assertEqual(user.full_name, 'Django Reinhardt')


class LiveUserTests(SeleniumTestCase):

    def visit_page(self, path):
        url = '%s%s' % (self.live_server_url,  path)
        return self.browser.get(url)

    @skipIf(not settings.SELENIUM_TESTS_ENABLED, 'Selenium tests skipped by config.')
    def test_user_list(self):
        response = self.visit_page('/users/')
        li = self.browser.find_element_by_tag_name('li')
        self.assertEqual(li.text, 'Django Reinhardt')
