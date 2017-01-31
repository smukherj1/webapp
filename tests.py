import unittest
import os

from wsgi import app

class WebappTest(unittest.TestCase):
    def setUp(self):
        os.environ['WEBAPP_UNIT_TEST'] = '1'
        app.config['WTF_CSRF_ENABLED'] = False
        self.app = app.test_client()
        r = self.app.get('/reset_db')
        os.environ.pop('WEBAPP_UNIT_TEST')
        assert(r.status_code == 200)
        return

    def tearDown(self):
        return

    def __test_get(self, url, status_code=200):
        with self.app.get(url) as resp:
            self.assertEqual(status_code, resp.status_code)
        return

    def test_get_index(self):
        self.__test_get('/')
        return

    def test_get_favicon(self):
        self.__test_get('/favicon.ico')
        return

    def test_get_style_css(self):
        self.__test_get('/static/css/style.css')
        return

    def test_get_login(self):
        self.__test_get('/login')
        return

    def test_get_register(self):
        self.__test_get('/register')
        return

    def __register(self, username, password, email):
        return self.app.post('/register', data=dict(
            username=username,
            password=password,
            email=email
            ),
            follow_redirects=True)

    def __check_homepage(self, resp, username):
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('Hello %s!'%username in str(resp.data))

    def __check_register(self, username, password, email):
        resp = self.__register(username, password, email)
        self.__check_homepage(resp, username)

    def test_registration(self):
        self.__check_register('test', 'test', 'test@test.com')
        return

    def __login(self, username, password):
        return self.app.post('/login', data=dict(
                    username=username,
                    password=password
                ),
                follow_redirects=True)

    def __logout(self):
        self.__test_get('/logout', 302)
        return

    def test_login(self):
        self.__register('test', 'test', 'test@test.com')
        self.__logout()
        # Log back in
        resp = self.__login('test', 'test')
        self.__check_homepage(resp, 'test')
        return

    def test_register_and_login_many(self):
        NUM_USERS = 10
        for i in range(NUM_USERS):
            self.__check_register('test%d'%i, 'test%d'%i, 'test@test.com')
            self.__logout()
        for i in range(NUM_USERS):
            resp = self.__login('test%d'%i, 'test%d'%i)
            self.__check_homepage(resp, 'test%d'%i)
            self.__logout()
        return


if __name__ == '__main__':
    unittest.main()
