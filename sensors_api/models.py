from secrets import choice
from django.db import models

# Create your models here.

TYPE = [
    ('', 'Type'),
    ("Temperature", "Temperature"),
    ("Humidity", "Humidity"),
    ("Acoustic", "Acoustic")
]

class Sensors(models.Model):
    sensor_id = models.AutoField(primary_key = True)
    type = models.CharField(max_length = 50,choices=TYPE)
    vendor_name = models.CharField(max_length = 50)
    vendor_email = models.EmailField(max_length = 255)
    description = models.TextField(max_length = 500)
    location = models.CharField(max_length = 50)

class Readings(models.Model):
    reading_id = models.AutoField(primary_key = True)
    sensor = models.ForeignKey(Sensors, on_delete = models.CASCADE)
    reading_type = models.CharField(max_length = 50)
    value = models.CharField(max_length = 50)
    date = models.DateField()
    description = models.TextField(max_length = 500)
    time = models.CharField(max_length = 50)