#!/bin/sh
#docker run -d --name sonarqube -e SONAR_ES_BOOTSTRAPCHECKS_DISABLE=true -p 9000:9000 -p 9092:9092 sonarqube:latest
# docker run --name=sensorsapi_jenkins --privileged -p 8080:8080 -p 50000:50000 -d -v /var/run/docker.sock:/var/run/docker.sock -v jenkins_home:/var/jenkins_home jenkins/jenkins:lts
#docker exec -it -u0 sensorsapi_jenkins bash 
#curl https://get.docker.com/ > dockerinstall && chmod 777 dockerinstall && ./dockerinstall
# sudo chmod 666 /var/run/docker.sock
# curl https://cli-assets.heroku.com/install-ubuntu.sh | sh
# sudo curl -L https://github.com/docker/compose/releases/download/1.21.0/docker-compose-`uname -s`-`uname -m` | sudo tee /usr/local/bin/docker-compose > /dev/null

docker run -d --name=jenkins --privileged -v jenkins_home:/var/jenkins_home -v /var/run/docker.sock:/var/run/docker.sock -p 8080:8080 -p 50000:50000 --restart=on-failure jenkins/jenkins:lts-jdk11