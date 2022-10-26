#!/bin/sh

python3 manage.py collectstatic --noinput
python3 manage.py makemigrations --noinput
python3 manage.py migrate --noinput

gunicorn SensorsAPI.wsgi:application --bind 0.0.0.0:$PORT