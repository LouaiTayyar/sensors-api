# create heroku app
#heroku create sensors-readings

# heroku login to container registry
#heroku container:login

# add postgresql database to heroku app
#heroku addons:create heroku-postgresql:hobby-dev -a sensors-readings


# build our heroku-ready local Docker image
docker build -t sensors-heroku .

# push your directory container for the web process to heroku
heroku container:push web -a sensors-readings

# promote the web process with your container 
heroku container:release web -a sensors-readings