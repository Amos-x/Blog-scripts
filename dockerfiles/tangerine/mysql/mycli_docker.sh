#!/usr/bin/env bash
source /home/apps/dockerfiles/tangerine/mysql/mysql_conf.sh

mycli -h ${HOST} -P ${PORT} -u${USERNAME} -p${PASSWORD}