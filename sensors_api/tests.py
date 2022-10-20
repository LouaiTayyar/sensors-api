from cmath import exp
from genericpath import samefile
import json
from random import sample
from rest_framework.test import APITestCase, APIRequestFactory
from .views import SensorsAPIView, ReadingsAPIView 
from django.urls import reverse
from rest_framework import status

class SensorsAPIViewTestCase(APITestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = SensorsAPIView.as_view()
        self.url = reverse('sensors')

    def test_post(self):

        sample_data = {
            'sensor_id': 1,
            'type': 'Temperature Sensor',
            'vendor_name': 'sample name',
            'vendor_email': 'sample@email.com',
            'description': 'description',
            'location': 'location'
        }

        response = self.client.post(self.url, sample_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get(self):

        response = self.client.get(self.url, {'sensor_id': 1})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], 'No sensors found')


        sample_data = {
            'sensor_id': 1,
            'type': 'Temperature Sensor',
            'vendor_name': 'sample name',
            'vendor_email': 'sample@email.com',
            'description': 'description',
            'location': 'location'
        }
        self.client.post(self.url, sample_data)

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)

    def test_put(self):
        pass