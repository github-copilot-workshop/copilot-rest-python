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


class VmsAPITestCase(APITestCase):
    api_path = '/api/vms/'

    def test_get_vms(self):
        response = self.client.get(self.api_path)

        # Check if the response status code is 200
        self.assertEqual(response.status_code, 200)

        # The response content should be an array
        response_data = json.loads(response.content)
        self.assertIsInstance(response_data, list)


# Additional tests for VmsDataAPITestCase to validate the API based on the data in vms.json

class VmsDataAPITestCase(APITestCase):
    api_path = '/api/vms/'

    # Existing test_get_vms method...

    def test_vms_data_validation(self):
        expected_vms_data = [
            {"size": "Standard_D2_v3", "vcpu": 2, "memory": 8},
            {"size": "Standard_D4_v3", "vcpu": 4, "memory": 16},
            {"size": "Standard_D8_v3", "vcpu": 8, "memory": 32},
            {"size": "Standard_D16_v3", "vcpu": 16, "memory": 64},
            {"size": "Standard_D32_v3", "vcpu": 32, "memory": 128},
            {"size": "Standard_D48_v3", "vcpu": 48, "memory": 192},
            {"size": "Standard_D64_v3", "vcpu": 64, "memory": 256},
        ]

        response = self.client.get(self.api_path)
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.content)

        # Ensure the response contains the correct number of VMs
        self.assertEqual(len(response_data), len(expected_vms_data))

        # Validate each VM's data
        for vm_data in expected_vms_data:
            self.assertIn(vm_data, response_data)