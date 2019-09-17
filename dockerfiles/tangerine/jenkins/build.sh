#!/usr/bin/env bash


useradd -g jenkins jenkins
docker stop myjenkins
docker rm myjenkins
mkdir /home/jenkins_data
chown -R jenkins. /home/jenkins_data
docker run -d -p 10010:8080 --name myjenkins -v /home/jenkins_data:/var/jenkins_home -t jenkins:last
# docker container prune
docker logs myjenkins