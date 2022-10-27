#!/bin/sh
# docker run --name=sensorsapi_jenkins --privileged -p 8080:8080 -p 50000:50000 -d -v /var/run/docker.sock:/var/run/docker.sock -v jenkins_home:/var/jenkins_home jenkins/jenkins:lts
docker exec -it -u0 sensorsapi_jenkins bash 
curl https://get.docker.com/ > dockerinstall && chmod 777 dockerinstall && ./dockerinstall
sudo chmod 666 /var/run/docker.sock
curl https://cli-assets.heroku.com/install-ubuntu.sh | sh

