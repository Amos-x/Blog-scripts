#!/usr/bin/env bash

source conf.sh

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


docker run --privileged=true -d --name ${docker_container_name} --publish ${server_port}:${internet_port}  -d zookeeper:latest

#参数说明：
#--privileged=true：容器内的root拥有真正root权限，否则容器内root只是外部普通用户权限
#-v ${productdirdata}/docker/redis/conf/redis.conf:/etc/redis/redis.conf：映射配置文件
#-v ${productdirdata}/docker/redis/data:/data：映射数据目录
# redis-server /etc/redis/redis.conf：指定配置文件启动redis-server进程
#--appendonly yes：开启数据持久化

# 创建命令工具
create_toolkit $server


