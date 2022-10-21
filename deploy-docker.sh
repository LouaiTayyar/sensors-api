docker-compose up -d --build
docker exec -it sensorsapi_api_1 python3 manage.py collectstatic --noinput
docker exec -it sensorsapi_api_1 python3 manage.py makemigrations --noinput
docker exec -it sensorsapi_api_1 python3 manage.py migrate --noinput
docker exec -it sensorsapi_api_1 python3 manage.py test --noinput