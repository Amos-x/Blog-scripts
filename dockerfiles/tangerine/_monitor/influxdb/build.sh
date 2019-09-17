#!/usr/bin/env bash

source ../conf.sh

#ENV_VAR=$1
#for var in ${ENV_ARR[*]}
#do
#    if [ "$ENV_VAR" != "$var" ];
#    then
#        echo "传入的第一个参数为:\"" $ENV_VAR "\" ,需要匹配下列单词: " ${ENV_ARR[*]}
#        echo "\n"
#        exit
#    fi
#done


# init 变量
product_docker_server_home=${DOCKER_VALUME}/${influxdb_server}/${influxdb_server_port}
mkdir -p ${product_docker_server_home}/influxdb


docker run -d -p ${influxdb_server_port}:${influxdb_internet_port}  -p ${influxdb_mgr_extranet_port}:${influxdb_mgr_intranet_port}  -v ${product_docker_server_home}/influxdb:/var/lib/influxdb  --name $influxdb_server  $influxdb_docker_version

# docker run -d -p8086:8086\-v ~/influxdb:/var/lib/influxdb \--name influxdb tutum/influxdb

# ./influxdb-test-toolkit 3 influx
# 创建数据库
# CREATE DATABASE "test"
# CREATE USER "root" WITH PASSWORD 'root' WITH ALL PRIVILEGES
# 创建命令工具
create_toolkit $influxdb_server

