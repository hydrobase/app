import unittest

from app import app


class TestDashboard(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.r = self.app.get('/dashboard')

    def tearDown(self):
        pass

    def test_dashboard_200(self):
        self.assertEquals(200, self.r.status_code)

    def test_dashboard_title(self):
        self.assertIn(b'<title>Your Dashboard</title>', self.r.data)


if __name__ == '__main__':
    unittest.main()