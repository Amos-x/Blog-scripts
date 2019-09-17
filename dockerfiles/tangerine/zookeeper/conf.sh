#!/usr/bin/env bash

source $COMMON_UTILS/init_start_script.sh

# 服务
server="zookeeper"-${ENV_VAR}

# 内网端口
server_port=2181

# 外网端口
internet_port=2181

# 服务名称
docker_container_name="zookeeper"-${ENV_VAR}
