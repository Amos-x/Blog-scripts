#!/bin/bash
# __author__ = Amos
#      Email = 379833553@qq.com
#  Create_at = 2018/11/14 下午12:03
#   FileName = ${NAME}


if [ ! -f "/etc/yum.repos.d/docker-ce.repo" ]; then
    cd /etc/yum.repos.d/
    wget https://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo
    yum install docker-ce -y
    systemctl enable docker
    systemctl restart docker
else
    echo "docker in existed, skip install"
fi
