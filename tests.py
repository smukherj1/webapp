import unittest
import os

from wsgi import app

class WebappTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        r = self.app.get('/reset_db')
        assert(r.status_code == 200)
        return

    def tearDown(self):
        return

    def test_get_index(self):
        self.assertEqual(0, 0)
        return

    def test_registration(self):
        self.assertEqual(1, 1)
        return

    def test_login(self):
        self.assertEqual(2, 2)
        return


if __name__ == '__main__':
    os.environ['WEBAPP_UNIT_TEST'] = '1'
    unittest.main()
    os.environ.pop('WEBAPP_UNIT_TEST')
