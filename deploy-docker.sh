docker-compose up -d --build
docker exec -it sensorsapi_api python3 manage.py collectstatic --noinput
docker exec -it sensorsapi_api python3 manage.py makemigrations --noinput
docker exec -it sensorsapi_api python3 manage.py migrate --noinput
docker exec -it sensorsapi_api python3 manage.py test --noinput