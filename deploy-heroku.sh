# create heroku app
#heroku create sensors-readings
heroku container:login
docker login --username=louaitayyar@outlook.com --password=0b6f1966-8fb7-48bf-9118-5f44067dd66e registry.heroku.com
docker build -t registry.heroku.com/sensors-readings/web .
docker push registry.heroku.com/sensors-readings/web 
heroku container:release web -a sensors-readings
# heroku login to container registry
#aaaaa
#aaaaaa
#aaaaa
#aaaa
# add postgresql database to heroku app
#heroku addons:create heroku-postgresql:hobby-dev -a sensors-readings


# build our heroku-ready local Docker image
#docker build -t sensorsapi_api .

# push your directory container for the web process to heroku
#heroku container:push web -a sensors-readings

# promote the web process with your container 
#heroku container:release web -a sensors-readings