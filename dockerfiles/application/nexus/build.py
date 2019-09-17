# -*- coding:utf-8 -*-
# __author__ = Amos
#      Email = 379833553@qq.com
#  Create_at = 2018/11/8 下午4:54
#   FileName = build

from utils.common import exec_shell,container_is_exist


def build_nexus():
    if not container_is_exist('nexus'):
        exec_shell('docker pull sonatype/nexus:2.14.10')
        exec_shell('docker run -d --name nexus --restart=always -p 8081:8081  sonatype/nexus:2.14.10')
        exec_shell('docker start nexus')
    else:
        print('nexus 容器已存在，跳过安装')
