#!/usr/bin/env bash


# harbor
#http://112.74.48.117:8082
#admin
#oracle
#
#cd /home/harbor && docker-compose restart
#cd /home/harbor && docker-compose stop
#
## harbor ssl
## 服务端
#openssl genrsa -out /home/harbor/certs/ca.key 2048
#openssl req -x509 -new -nodes -key /home/harbor/certs/ca.key -subj "/CN=112.74.48.117" -days 5000 -out /home/harbor/certs/ca.crt
#
#
## 客户端
#mkdir -p /etc/docker/certs.d/112.74.48.117


# 向harbor推送镜像
docker tag wise2c/keepalived-k8s 112.74.48.117:8082/temp/keepalived-k8s
docker push 112.74.48.117:8082/temp/keepalived-k8s
docker login -u admin -p oracle 172.18.73.129