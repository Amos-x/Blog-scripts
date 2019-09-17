#!/usr/bin/env bash


# 连接资源
PASSWORD="oracle"
USERNAME="root"
PORT=3306

# 打包机
HOST=`ifconfig | grep 'inet'| grep -v '127.0.0.1'|grep -v "172.17.0.1" | cut -d: -f2 | awk '{ print $2}'`
#HOST="172.18.73.129"


