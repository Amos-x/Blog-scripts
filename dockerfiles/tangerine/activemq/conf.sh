#!/usr/bin/env bash

source $COMMON_UTILS/init_start_script.sh

# 服务
server="activemq"-${ENV_VAR}

# 内网服务端口
web_server_port=61616

# 外网服务端口
web_internet_port=61616

# 内网后台端口
console_server_port=8161

# 外网后台端口
console_internet_port=8161

# 服务名称
docker_version="docker.io/webcenter/activemq:latest"



