#!/usr/bin/env bash

source $COMMON_UTILS/init_start_script.sh

# 服务
server="mysql5.6"-${ENV_VAR}

# 内网服务端口
web_server_port=3306

# 外网服务端口
web_internet_port=3306

# 服务名称
docker_version="mysql:5.6"







