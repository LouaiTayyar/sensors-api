# this is a script used in devlopment to remove docker containers, image, and volumes

docker stop $(docker ps -aq)
docker rm $(docker ps -aq)
docker rmi $(docker images -aq) -f
docker volume prune -f

