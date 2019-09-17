#!/usr/bin/env bash

source $COMMON_UTILS/init_start_script.sh

# 服务
server="redis"-$ENV_VAR

# 内网端口
server_port=6379

# 外网端口
internet_port=6379

# 服务名称
docker_container_name="redis"-$ENV_VAR