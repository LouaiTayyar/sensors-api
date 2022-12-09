#!/bin/sh
chmod 777 /var/run/docker.sock
python3 manage.py collectstatic --noinput
python3 manage.py makemigrations --noinput
python3 manage.py migrate --noinput
gunicorn sensors_project.wsgi:application --bind 0.0.0.0:$PORT

#testaaa
