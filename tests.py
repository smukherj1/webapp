import unittest
import os

from wsgi import app

class WebappTest(unittest.TestCase):
    def setUp(self):
        os.environ['WEBAPP_UNIT_TEST'] = '1'
        self.app = app.test_client()
        r = self.app.get('/reset_db')
        os.environ.pop('WEBAPP_UNIT_TEST')
        assert(r.status_code == 200)
        return

    def tearDown(self):
        return

    def __test_get(self, url):
        with self.app.get(url) as resp:
            self.assertEqual(200, resp.status_code)
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

    def test_registration(self):
        self.assertEqual(1, 1)
        return

    def test_login(self):
        self.assertEqual(2, 2)
        return


if __name__ == '__main__':
    unittest.main()
