#!/usr/bin/env bash


# base server
docker pull redis:4.0
docker pull zookeeper:latest
docker pull docker.io/webcenter/activemq:latest

docker pull nginx:latest
docker pull  mysql:5.6

docker pull  tutum/influxdb