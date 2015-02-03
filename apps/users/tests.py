from django.test import TestCase, LiveServerTestCase
from apps.users.factories import UserFactory
from apps.users.models import User
from selenium import webdriver

class UserTests(TestCase):

    def test_full_name(self):
        user = UserFactory.create(first_name='Django', last_name='Reinhardt')
        self.assertEqual(user.full_name, 'Django Reinhardt')


class LiveUserTests(LiveServerTestCase):

    def setUp(self):
        User.objects.create(first_name='Django', last_name='Reinhardt', username='django')
        self.browser = webdriver.Firefox()
        super(LiveUserTests, self).setUp()

    def tearDown(self):
        self.browser.quit()

    def visit_page(self, path):
        url = '%s%s' % (self.live_server_url,  path)
        return self.browser.get(url)

    def test_user_list(self):
        response = self.visit_page('/users/')
        li = self.browser.find_element_by_tag_name('li')
        self.assertEqual(li.text, 'Django Reinhardt')
