from rest_framework import serializers
from sensors_api.models import Sensors,Readings


class SensorsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Sensors
		fields = '__all__'

class ReadingsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Readings
		fields = '__all__'