from apps.auth_user.models import User
from utils.testbase import BaseWebTest


class APITest(BaseWebTest):
    fixtures = ['deploy/init_user.json']

    def setUp(self):
        self.admin_header = {'Authorization': "Token %s" % str(User.objects.get(username='admin').get_token())}
        super(APITest, self).setUp()
