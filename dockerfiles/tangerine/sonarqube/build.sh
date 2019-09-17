#!/usr/bin/env bash


# sonarqube
docker run --name postgresql -p 5431:5432 -e POSTGRES_USER=sonar -e POSTGRES_PASSWORD=sonar -e POSTGRE_DB=sonar -d postgres
docker run --name sonarqube --link postgresql -e SONARQUBE_JDBC_URL=jdbc:postgresql://172.18.73.129:5431/sonar -p 9000:9000 -d sonarqube

#http://112.74.48.117:9000
#admin admin
#
#
#sonar-scanner -Dsonar.projectKey=test -Dsonar.projectName=test -Dsonar.projectVersion=1.0 -Dsonar.sources=src -Dsonar.language=java
#mvn sonar:sonar \
#    sonar-scanner\
#  -Dsonar.projectKey=test\
#  -Dsonar.projectName=test\
#  -Dsonar.projectVersion=1.0\
#  -Dsonar.sources=src\
#  -Dsonar.language=java\
#  -Dsonar.host.url=http://112.74.48.117:9000 \
#  -Dsonar.login=0986766c4182bf9fee00aed4bc82541129f77c7c
#tangerine: 0986766c4182bf9fee00aed4bc82541129f77c7c
docker restart sonarqube
