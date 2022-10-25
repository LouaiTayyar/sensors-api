from venv import create
from .models import Sensors,Readings
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from .serializers import SensorsSerializer, ReadingsSerializer

def create_test_sensor():
    sensor = Sensors.objects.create(
        sensor_id = 1,
        type = 'Temperature Sensor',
        vendor_name = 'sample name',
        vendor_email = 'sample@email.com',
        description = 'description',
        location = 'location')
    return sensor

def create_test_reading(sensor):
    reading = Readings.objects.create(
    reading_id = 1,
    sensor = sensor,
    type = 'type',
    value = 'value',
    date = '2022-10-11',
    description = 'description',
    time = 'time'
    )    
    return reading  

test_sensor_data = {
            'sensor_id': 1,
            'type': 'Temperature Sensor',
            'vendor_name': 'sample name',
            'vendor_email': 'sample@email.com',
            'description': 'description',
            'location': 'location'
        }

test_reading_data = {
            'sensor': 1,
            'type': 'type',
            'value': 'value',
            'date': '2022-10-11',
            'description': 'description',
            'time': 'time'
        }

class CreateSensorsTest(APITestCase):

    def setUp(self):
        self.url = reverse('sensors')
        self.data = test_sensor_data

    def test_can_create_sensor(self):
        response = self.client.post(self.url, self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class ReadSensorsTest(APITestCase):

    def setUp(self):
        self.url = reverse('sensors')
        self.sensor = create_test_sensor()
        self.sensor_detail_url = self.url + '?sensor_id=1'

    def test_can_read_sensor_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_read_sensor_detail(self):
        response = self.client.get(self.sensor_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UpdateSensorsTest(APITestCase):

    def setUp(self):
        self.url = reverse('sensors')
        self.sensor = create_test_sensor()
        self.sensor_detail_url = self.url + '?sensor_id=1'
        self.data = SensorsSerializer(self.sensor).data
        self.data.update({'type': 'Humidity Sensor'})
            
    def test_can_update_sensor(self):
        response = self.client.put(self.sensor_detail_url, self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class DeleteSensorsTest(APITestCase):

    def setUp(self):
        self.url = reverse('sensors')
        self.sensor = create_test_sensor()
        self.sensor_detail_url = self.url + '?sensor_id=1'
            
    def test_can_delete_sensor(self):
        response = self.client.delete(self.sensor_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CreateReadingsTest(APITestCase):

    def setUp(self):
        self.url = reverse('readings')
        self.sensor = create_test_sensor()
        self.data = test_reading_data

    def test_can_create_reading(self):
        response = self.client.post(self.url, self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class ReadReadingsTest(APITestCase):

    def setUp(self):
        self.url = reverse('readings')
        self.sensor = create_test_sensor()
        self.reading = create_test_reading(self.sensor)      
        self.reading_detail_url = self.url + '?sensor_type=Temperature Sensor&sensor_location=location&time=12:00'

    def test_can_read_reading_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_read_reading_detail(self):
        response = self.client.get(self.reading_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UpdateReadingsTest(APITestCase):

    def setUp(self):
        self.url = reverse('readings')
        self.sensor = create_test_sensor()
        self.reading = create_test_reading(self.sensor)      
        self.reading_detail_url = self.url + '?reading_id=1'
        self.data = ReadingsSerializer(self.reading).data
        self.data.update({'type': 'updated type'})
            
    def test_can_update_sensor(self):
        response = self.client.put(self.reading_detail_url, self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class DeleteReadingsTest(APITestCase):

    def setUp(self):
        self.url = reverse('readings')
        self.sensor = create_test_sensor()
        self.reading = create_test_reading(self.sensor)      
        self.reading_detail_url = self.url + '?reading_id=1'
            
    def test_can_delete_reading(self):
        response = self.client.delete(self.reading_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)