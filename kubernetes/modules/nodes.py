# -*- coding:utf-8 -*-
# __author__ = Amos
#      Email = 379833553@qq.com
#  Create_at = 2018/12/7 上午9:41
#   FileName = nodes

from utils.common import send_files,FileModify,parse_address,exec_shell,SSHConnect,check_is_localip
from kubernetes.settings import settings as SETTINGS
from kubernetes.util import get_cfssl_dir,get_etcd_endpoints
import os
import json
import time

TEMPLATE_DIR = SETTINGS.TEMPLATE_DIR
FILES_DIR = SETTINGS.FILES_DIR
VERSION = SETTINGS.VERSION
IPS = SETTINGS.IPS

