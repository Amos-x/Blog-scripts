#!/usr/bin/env bash

source $COMMON_UTILS/init_start_script.sh

# 服务
influxdb_server="influxdb"-${ENV_VAR}

# 内网服务端口
influxdb_server_port=10015

# 外网服务端口
influxdb_internet_port=8086

# 管理端口
influxdb_mgr_extranet_port=10019
influxdb_mgr_intranet_port=8083

# 服务名称
docker_container_influxdb="influxdb"
influxdb_docker_version=" tutum/influxdb"

# influxdb 账号密码
username="root"
password="root"
db="test"

# influxdb 链接
# docker exec-it influxdb influx



# 服务
cadvisor_server="cadvisor"-${ENV_VAR}

# 服务名称
cadvisor_docker_version="google/cadvisor:v0.27.3"



# 服务
grafana_server="grafana"-${ENV_VAR}

# 内网服务端口
grafana_extranet_port=10010

# 外网服务端口
grafana_intranet_port=3000

# 服务名称
grafana_docker_version="grafana/grafana "




