from rest_framework.test import APITestCase
from rest_framework.utils import json

class TimeAPITestCase(APITestCase):
    api_path = '/api/time/'

    def test_get_current_time(self):
        response = self.client.get(self.api_path)
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.content)
        self.assertIn('time', response_data)
        self.assertIsNotNone(response_data['time'])

class HelloAPITestCase(APITestCase):
    api_path = '/api/hello/'

    def test_get_hello(self):
        response = self.client.get(self.api_path)
        self.assertEqual(response.status_code, 501)
        response_data = json.loads(response.content)
        self.assertIn('message', response_data)
        self.assertEqual(response_data['message'], 'key query parameter is required')

    def test_get_hello_with_key(self):
        response = self.client.get(self.api_path, {'key': 'World'})
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.content)
        self.assertIn('message', response_data)
        self.assertEqual(response_data['message'], 'Hello World')