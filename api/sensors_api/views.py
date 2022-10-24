from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Sensors,Readings
from sensors_api.serializers import SensorsSerializer, ReadingsSerializer
from rest_framework.pagination import PageNumberPagination

# Sensors API view

class SensorsAPIView(APIView):
    serializer = SensorsSerializer

    def get(self,request):
        
        sensor_id = request.query_params.get('sensor_id',None)

        if sensor_id:
            sensors = Sensors.objects.filter(sensor_id = sensor_id)
        else:
            sensors = Sensors.objects.all()

        if sensors:
            sensors_serializer = self.serializer(sensors, many=True)
            return Response(sensors_serializer.data, status = status.HTTP_200_OK)
        else:
            return Response({'message':'No sensors found'}, status = status.HTTP_200_OK)

    def post(self,request):
    
        sensor_id = request.data.get('sensor_id',None)
        type = request.data.get('type',None)
        vendor_name = request.data.get('vendor_name',None)
        vendor_email = request.data.get('vendor_email',None)
        description = request.data.get('description',None)
        location = request.data.get('location',None)

        post_data = {
            'sensor_id': sensor_id,
            'type': type,
            'vendor_name': vendor_name,
            'vendor_email': vendor_email,
            'description': description,
            'location': location
        }

        serializer = self.serializer(data = post_data)
        if serializer.is_valid(raise_exception = True):
            sensor = serializer.save()
        
        if sensor:
            return Response({'message':'Successful new sensor added'}, status = status.HTTP_201_CREATED)
        else:
            return Response({'message':'Something went wrong'}, status = status.HTTP_400_BAD_REQUEST)

    def put(self,request):
        
        sensor_id = request.query_params.get('sensor_id',None)

        if sensor_id:
            sensor = Sensors.objects.get(sensor_id = sensor_id)
        else:
            sensor = None
            
        if not sensor:
            return Response({'message':'Sensor not found'}, status = status.HTTP_404_NOT_FOUND)
        
        type = request.data.get('type', None)
        if type:
            sensor.type = type
            sensor.save()

        vendor_name = request.data.get('vendor_name',None)
        if vendor_name:
            sensor.vendor_name = vendor_name
            sensor.save()

        vendor_email = request.data.get('vendor_email',None)
        if vendor_email:
            sensor.vendor_email = vendor_email
            sensor.save()

        description = request.data.get('description',None)
        if description:
            sensor.description = description
            sensor.save()

        location = request.data.get('location',None)
        if location:
            sensor.location = location
            sensor.save()
        
        return Response({'message':'Sensor updated'}, status = status.HTTP_200_OK)

    def delete(self,request):
        
        sensor_id = request.query_params.get('sensor_id',None)
        sensor = Sensors.objects.get(sensor_id = sensor_id)

        if not sensor:
            return Response({'message':'Sensor not found'}, status = status.HTTP_404_NOT_FOUND)
        
        sensor.delete()
        return Response({'message':'Sensor removed'},status = status.HTTP_200_OK)



# Sensor Readings API view

class ReadingsAPIView(APIView):
    serializer = ReadingsSerializer
    paginator = PageNumberPagination()


    def get(self,request):
        
        sensor_type = request.query_params.get('sensor_type',None)
        sensor_location = request.query_params.get('sensor_location',None)
        time = request.query_params.get('time',None)
        readings = Readings.objects.all()

        if sensor_type:
            readings = readings.filter(sensor__type = sensor_type)
        if sensor_location:
            readings = readings.filter(sensor__location = sensor_location)
        if time:
            readings = readings.filter(time = time)
            
        if readings:
            result_page = self.paginator.paginate_queryset(readings, request)
            reading_serializer = self.serializer(result_page, many=True, context={'request':request})
            metrics = get_metrics(readings)
            dict = {
                'readings' : reading_serializer.data,
                'metrics': metrics
            }
            return Response(dict, status = status.HTTP_200_OK)
        else:
            return Response({'message':'No readings found'}, status = status.HTTP_200_OK)

    def post(self,request):
    
        reading_id = request.data.get('reading_id',None)
        sensor_id = request.data.get('sensor',None)
        type = request.data.get('type',None)
        value = request.data.get('value',None)
        date = request.data.get('date',None)
        description = request.data.get('description',None)
        time = request.data.get('time',None)

        post_data = {
            'reading_id': reading_id,
            'sensor': sensor_id,
            'type': type,
            'value': value,
            'date': date,
            'description': description,
            'time': time
        }

        serializer = self.serializer(data = post_data)
        if serializer.is_valid(raise_exception = True):
            reading = serializer.save()
        
        if reading:
            return Response({'message':'Successful new reading added'}, status = status.HTTP_201_CREATED)
        else:
            return Response({'message':'Something went wrong'}, status = status.HTTP_400_BAD_REQUEST)

    def put(self,request):
        
        reading_id = request.query_params.get('reading_id',None)

        reading = Readings.objects.get(reading_id = reading_id)

        if not reading:
            return Response({'message':'Reading not found'}, status = status.HTTP_404_NOT_FOUND)
        
        sensor_id = request.data.get('sensor_id',None)
        if sensor_id:
            reading.sensor = Sensors.objects.get(sensor_id = sensor_id)
            reading.save()

        reading_type = request.data.get('reading_type',None)
        if reading_type:
            reading.reading_type = reading_type
            reading.save()

        value = request.data.get('value',None)
        if value:
            reading.value = value
            reading.save()

        date = request.data.get('date',None)
        if date:
            reading.date = date
            reading.save()

        description = request.data.get('description',None)
        if description:
            reading.description = description
            reading.save()

        time = request.data.get('time',None)
        if time:
            reading.time = time
            reading.save()

        return Response({'message':'Reading updated'},status = status.HTTP_200_OK)

    def delete(self,request):
        
        reading_id = request.query_params.get('reading_id', None)
        reading = Readings.objects.get(reading_id = reading_id)

        if not reading:
            return Response({'message':'Reading not found'}, status = status.HTTP_404_NOT_FOUND)
        
        reading.delete()
        return Response({'message':'Reading removed'},status = status.HTTP_200_OK)

# Helper functions

def get_metrics(readings):

    values_list = []
    extra_info = {}
    for reading in readings:
        value_is_number = is_float(reading.value)
        if (value_is_number):
            values_list.append(float(reading.value))
    if len(values_list) != 0:
        value_range = get_value_range(values_list)
        mean_value = get_mean_value(values_list)
        max_records = get_max_records(values_list)
        min_records = get_min_records(values_list)
        extra_info = {
            'value_range': value_range,
            'mean_value': mean_value,
            'max_records': max_records,
            'min_records': min_records,
        }
    return extra_info

def is_float(reading_value):

    try:
        float(reading_value)
        return True
    except:
        return False

def get_value_range(values_list):

    min_value = min(values_list)
    max_value = max(values_list)
    value_range = (min_value,max_value)

    return value_range

def get_mean_value(values_list):

    mean_value = sum(values_list) / len(values_list)

    return mean_value

def get_max_records(values_list):

    num_of_records = min(10,len(values_list))
    values_list.sort(reverse = True)
    max_records = []
    for i in range(0,num_of_records):
        max_records.append(values_list[i])

    return max_records

def get_min_records(values_list):

    num_of_records = min(10,len(values_list))
    values_list.sort()
    min_records = []
    for i in range(0,num_of_records):
        min_records.append(values_list[i])

    return min_records