from django.test import TestCase


# LandingPage of test.
class HomeTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/')

    def test_get(self):
        """test of should status code 200"""
        self.assertEqual(200, self.resp.status_code)
