from base_test_case import BaseTestCase


class TestCase(BaseTestCase):

    def test_login(self):
        for login, password in self.auth.items():
            # print('login:', login)
            # print('password:', password)
            pass
