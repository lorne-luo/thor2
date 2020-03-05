from django.test.client import Client
from django_webtest import WebTest


class BaseWebTest(WebTest):
    def setUp(self):
        super(BaseWebTest, self).setUp()

        self.client = Client()

        login_success = self.client.login(username='admin', password='admin')
        self.assertTrue(login_success)
