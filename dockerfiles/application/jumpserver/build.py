# -*- coding:utf-8 -*-
# __author__ = Amos
#      Email = 379833553@qq.com
#  Create_at = 2018/11/8 下午5:01
#   FileName = build

from utils.common import exec_shell,container_is_exist


def build_jumpserver():
    if not container_is_exist('jumpserver'):
        exec_shell('docker pull harbor.yaobili.com/apps/jumpserver:latest')
        exec_shell('docker run -d --name jumpserver -p 8000:80 -p 2222:2222 harbor.yaobili.com/apps/jumpserver:latest')
    else:
        print('jumpserver 容器已存在，跳过安装')
