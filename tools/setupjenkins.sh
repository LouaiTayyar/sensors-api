#!/bin/sh
#docker run -d --name sonarqube -e SONAR_ES_BOOTSTRAPCHECKS_DISABLE=true -p 9000:9000 -p 9092:9092 sonarqube:latest

docker run -d --name=jenkins --privileged -v jenkins_home:/var/jenkins_home -v /var/run/docker.sock:/var/run/docker.sock -p 8080:8080 -p 50000:50000 --restart=on-failure jenkins/jenkins:lts-jdk11
docker exec -it -u0 jenkins bash 
curl https://get.docker.com/ > dockerinstall && chmod 777 dockerinstall && ./dockerinstall
