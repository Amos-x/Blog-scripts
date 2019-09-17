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
product_docker_server_home=${DOCKER_VALUME}/${grafana_server}/${grafana_extranet_port}
mkdir -p ${product_docker_server_home}/grafana

# 由于docker 内外的权限位要一样  472 是grafana的官方的权限 外面没有这个用户所以需要把权限给他加上
chown -R 472:472 ${product_docker_server_home}/grafana


docker run -d -p ${grafana_extranet_port}:${grafana_intranet_port} -v $product_docker_server_home/grafana:/var/lib/grafana --link=$influxdb_server:$influxdb_server --name $grafana_server $grafana_docker_version


#docker run -d -p5000:3000\-v ~/grafana:/var/lib/grafana \--link=influxdb:influxdb \--name grafana grafana/grafana


# 创建命令工具
create_toolkit $grafana_server

