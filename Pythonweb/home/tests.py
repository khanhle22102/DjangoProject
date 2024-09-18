from django.test import TestCase, SimpleTestCase

class simpleTest(SimpleTestCase):
    def test_homepage_status(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

# Create your tests here.
