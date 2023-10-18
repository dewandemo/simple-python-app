import unittest
from app import app

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        # This method will be run before each test
        app.testing = True
        self.app = app.test_client()

    def test_hello(self):
        # Test the /hello/<name> endpoint
        response = self.app.get('/hello/John')
        self.assertEqual(response.data.decode(), 'Hello, John!')

    def test_health(self):
        # Test the /health endpoint
        response = self.app.get('/health')
        json_data = response.get_json()
        self.assertEqual(json_data['status'], 'healthy')

if __name__ == '__main__':
    unittest.main()
