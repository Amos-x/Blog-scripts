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


docker run -d  -v /cgroup:/cgroup:ro -v /:/rootfs -v /var/run:/var/run -v /sys:/sys  -v /var/lib/docker:/var/lib/docker  --link=$influxdb_server:$influxdb_server --name $cadvisor_server $cadvisor_docker_version --storage_driver=influxdb --storage_driver_host=${influxdb_server}:$influxdb_server_port --storage_driver_db=${db}  --storage_driver_user=${username}  --storage_driver_password=${password}


# --privileged=true
#docker run  -v /cgroup:/cgroup:ro -v /:/rootfs:ro -v /var/run:/var/run:rw -v /sys:/sys:ro -v /var/lib/docker/:/var/lib/docker:ro  --link=influxdb-test:influxdb-test --name cadvisor-test google/cadvisor:v0.27.3 --storage_driver=influxdb-test --storage_driver_host=influxdb-test:8086 --storage_driver_db=test  --storage_driver_user=root  --storage_driver_password=root


# docker run --rm=true --link=influxdb-test:influxdb -it google/cadvisor:v0.27.3 /bin/bash
# 创建命令工具
create_toolkit $cadvisor_server



