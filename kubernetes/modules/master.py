# -*- coding:utf-8 -*-
# __author__ = Amos
#      Email = 379833553@qq.com
#  Create_at = 2018/12/6 下午7:20
#   FileName = master

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


def hand_out_files():
    for i in IPS.get('master'):
        send_files(os.path.join(FILES_DIR,VERSION,'master','*'),'/opt/kubernetes/bin',i)
        send_files(os.path.join(TEMPLATE_DIR,'master','*.pem'),'/opt/kubernetes/ssl',i)
        send_files(os.path.join(TEMPLATE_DIR,'master','*.csv'),'/opt/kubernetes/ssl',i)
        send_files(os.path.join(TEMPLATE_DIR,'master','kube-scheduler.service'),'/usr/lib/systemd/system',i)


def init_ca():
    path = os.path.join(TEMPLATE_DIR, 'master', 'kubernetes-csr.json')
    f = FileModify(path)
    template_content = f.content()
    result = json.loads(template_content, encoding='UTF-8')
    for ip_ in IPS.get('master'):
        ip, port = parse_address(ip_)
        result['hosts'].append(ip)
    result['hosts'].append(SETTINGS.CLUSTER_KUBERNETES_SVC_IP)
    f.cover(json.dumps(result))
    cfssl_dir = get_cfssl_dir()
    os.chdir(os.path.join(TEMPLATE_DIR, 'master'))
    ca_dir = os.path.join(TEMPLATE_DIR, 'ca')
    exec_shell('{0}/cfssl gencert -ca={1}/ca.pem -ca-key={1}/ca-key.pem -config={1}/ca-config.json '
               '-profile=kubernetes kubernetes-csr.json | {0}/cfssljson -bare kubernetes'.format(cfssl_dir,ca_dir))
    exec_shell('{0}/cfssl gencert -ca={1}/ca.pem -ca-key={1}/ca-key.pem -config={1}/ca-config.json '
               '-profile=kubernetes admin-csr.json | {0}/cfssljson -bare admin'.format(cfssl_dir,ca_dir))
    f.cover(template_content)


def init_api_server_config():
    path = os.path.join(TEMPLATE_DIR,'master','kube-apiserver.service')
    f = FileModify(path)
    for i in IPS.get('master'):
        ip,port = parse_address(i)
        f.replace('(?<=--bind-address=).*','{} \\'.format(ip))
        f.replace('(?<=service-cluster-ip-range=).*','{} \\'.format(SETTINGS.SERVICE_CIDR))
        f.replace('(?<=service-node-port-range=).*','{} \\'.format(SETTINGS.NODE_PORT_RANGE))
        f.replace('(?<=etcd-servers=).*','{} \\'.format(get_etcd_endpoints()))
        send_files(os.path.join(TEMPLATE_DIR,'master','kube-apiserver.service'),'/usr/lib/systemd/system',i)


def init_controller_manager_config():
    path = os.path.join(TEMPLATE_DIR,'master','kube-controller-manager.service')
    f = FileModify(path)
    for i in IPS.get('master'):
        f.replace('(?<=service-cluster-ip-range=).*','{} \\'.format(SETTINGS.SERVICE_CIDR))
        f.replace('(?<=cluster-cidr=).*','{} \\'.format(SETTINGS.POD_CIDR))
        send_files(os.path.join(TEMPLATE_DIR,'master','kube-controller-manager.service'),'/usr/lib/systemd/system',i)


def start_service():
    for i in IPS.get('master'):
        ip,port = parse_address(i)
        ssh = SSHConnect(ip,int(port))
        ssh.run('systemctl daemon-reload && systemctl enable kube-apiserver && systemctl start kube-apiserver && '
                'systemctl status kube-apiserver && systemctl enable kube-controller-manager && '
                'systemctl start kube-controller-manager && systemctl status kube-controller-manager && '
                'systemctl enable kube-scheduler && systemctl start kube-scheduler && systemctl status kube-scheduler')


def set_kubectl():
    for i in IPS.get('master'):
        ip,port = parse_address(i)
        ssh = SSHConnect(ip,int(port))
        ssh.run('source /etc/profile && kubectl config set-cluster kubernetes '
                '--certificate-authority=/opt/kubernetes/ssl/ca.pem --embed-certs=true '
                '--server=https://{}:6443'.format(ip))
        ssh.run('source /etc/profile && kubectl config set-credentials admin '
                '--client-certificate=/opt/kubernetes/ssl/admin.pem --embed-certs=true '
                '--client-key=/opt/kubernetes/ssl/admin-key.pem')
        ssh.run('source /etc/profile && kubectl config set-context kubernetes --cluster=kubernetes --user=admin')
        ssh.run('source /etc/profile && kubectl config use-context kubernetes')


def check_health():
    for i in IPS.get('master'):
        ip,port = parse_address(i)
        ssh = SSHConnect(ip,int(port))
        ssh.run('source /etc/profile && kubectl get cs')


def build():
    init_ca()
    init_api_server_config()
    init_controller_manager_config()
    hand_out_files()
    start_service()
    set_kubectl()
    time.sleep(3)
    check_health()


if __name__ == '__main__':
    init_ca()