# -*- coding:utf-8 -*-
# __author__ = Amos
#      Email = 379833553@qq.com
#  Create_at = 2018/12/6 上午9:44
#   FileName = ca

from utils.common import send_files,exec_shell
from kubernetes.settings import settings as SETTINGS
from kubernetes.util import get_all_ip,get_cfssl_dir
import os

TEMPLATE_DIR = SETTINGS.TEMPLATE_DIR
IPS = SETTINGS.IPS


def hand_out_files():
    all_ip = get_all_ip(IPS)
    for ip in all_ip:
        send_files(os.path.join(TEMPLATE_DIR,'ca','*'),'/opt/kubernetes/ssl',ip)


def init_ca():
    cfssl_dir = get_cfssl_dir()
    exec_shell('chmod +x {}/*'.format(cfssl_dir))
    os.chdir(os.path.join(TEMPLATE_DIR,'ca'))
    exec_shell('{0}/cfssl gencert -initca ca-csr.json | {0}/cfssljson -bare ca'.format(cfssl_dir))


def build():
    init_ca()
    hand_out_files()
