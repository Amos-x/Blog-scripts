# -*- coding:utf-8 -*-
# __author__ = Amos
#      Email = 379833553@qq.com
#  Create_at = 2018/12/6 上午10:53
#   FileName = etcd

from utils.common import send_files,FileModify,parse_address,exec_shell,SSHConnect,check_is_localip
from kubernetes.settings import settings as SETTINGS
from kubernetes.util import get_cfssl_dir,get_etcd_cluster,get_etcd_endpoints
import os
import json
import time

TEMPLATE_DIR = SETTINGS.TEMPLATE_DIR
FILES_DIR = SETTINGS.FILES_DIR
VERSION = SETTINGS.VERSION
IPS = SETTINGS.IPS


def init_etcd_ca():
    path = os.path.join(TEMPLATE_DIR,'etcd','etcd-csr.json')
    f = FileModify(path)
    template_content = f.content()
    result = json.loads(template_content,encoding='UTF-8')
    for ip_ in IPS.get('etcd'):
        ip,port = parse_address(ip_)
        result['hosts'].append(ip)
    f.cover(json.dumps(result))
    cfssl_dir = get_cfssl_dir()
    os.chdir(os.path.join(TEMPLATE_DIR,'etcd'))
    exec_shell('{0}/cfssl gencert -ca={1}/ca.pem -ca-key={1}/ca-key.pem -config={1}/ca-config.json '
               '-profile=kubernetes etcd-csr.json | {0}/cfssljson -bare etcd'.format(cfssl_dir,os.path.join(TEMPLATE_DIR,'ca')))
    f.cover(template_content)


def init_config():
    path = os.path.join(TEMPLATE_DIR, 'etcd', 'etcd.conf')
    f = FileModify(path)
    etcd_cluster = get_etcd_cluster()
    f.replace('(?<=ETCD_INITIAL_CLUSTER=").*(?=")',etcd_cluster)
    etcd_cluster_dict = get_etcd_cluster('dict')
    for i in IPS.get('etcd'):
        ip,port = parse_address(i)
        f.replace('(?<=ETCD_NAME=").*(?=")',etcd_cluster_dict.get(ip))
        f.replace('(?<=ETCD_LISTEN_PEER_URLS=").*(?=")','https://{}:2380'.format(ip))
        f.replace('(?<=ETCD_LISTEN_CLIENT_URLS=").*(?=")','https://{}:2379,https://127.0.0.1:2379'.format(ip))
        f.replace('(?<=ETCD_INITIAL_ADVERTISE_PEER_URLS=").*(?=")','https://{}:2380'.format(ip))
        f.replace('(?<=ETCD_ADVERTISE_CLIENT_URLS=").*(?=")','https://{}:2379'.format(ip))
        send_files(path,'/opt/kubernetes/cfg/',i)


def hand_out_files():
    etcd_ips = IPS.get('etcd')
    for ip in etcd_ips:
        send_files(os.path.join(FILES_DIR,VERSION,'etcd','etcd*'),'/opt/kubernetes/bin',ip)
        send_files(os.path.join(TEMPLATE_DIR,'etcd','etcd*.pem'),'/opt/kubernetes/ssl',ip)
        send_files(os.path.join(TEMPLATE_DIR,'etcd','etcd.service'),'/etc/systemd/system',ip)


def start_service():
    for i in IPS.get('etcd'):
        ip,port = parse_address(i)
        cmd = 'mkdir -p mkdir /var/lib/etcd && systemctl daemon-reload && systemctl enable etcd ' \
              '&& systemctl start etcd && systemctl status etcd'
        if not check_is_localip(ip):
            ssh = SSHConnect(ip,int(port))
            ssh.run(cmd)
        else:
            exec_shell(cmd)


def check_health():
    etcd_endpoints = get_etcd_endpoints()
    cmd = 'source /etc/profile && etcdctl --endpoints={} --ca-file=/opt/kubernetes/ssl/ca.pem ' \
          '--cert-file=/opt/kubernetes/ssl/etcd.pem --key-file=/opt/kubernetes/ssl/etcd-key.pem ' \
          'cluster-health'.format(etcd_endpoints)
    for i in IPS.get('etcd'):
        ip,port = parse_address(i)
        if not check_is_localip(ip):
            ssh = SSHConnect(ip,int(port))
            ssh.run(cmd)
            ssh.close()
        else:
            exec_shell(cmd)


def build():
    init_etcd_ca()
    init_config()
    hand_out_files()
    start_service()
    time.sleep(3)
    check_health()


if __name__ == '__main__':
    pass
