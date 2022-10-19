# Generated by Django 4.1.2 on 2022-10-19 12:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Sensors",
            fields=[
                ("sensor_id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("Temperature", "Temperature"),
                            ("Humidity", "Humidity"),
                            ("Acoustic", "Acoustic"),
                        ],
                        max_length=50,
                    ),
                ),
                ("vendor_name", models.CharField(max_length=50)),
                ("vendor_email", models.EmailField(max_length=255)),
                ("description", models.TextField(max_length=500)),
                ("location", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Readings",
            fields=[
                ("reading_id", models.AutoField(primary_key=True, serialize=False)),
                ("reading_type", models.CharField(max_length=50)),
                ("value", models.CharField(max_length=50)),
                ("date", models.DateField()),
                ("description", models.TextField(max_length=500)),
                ("time", models.CharField(max_length=50)),
                (
                    "sensor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="sensors_api.sensors",
                    ),
                ),
            ],
        ),
    ]
