# -*- coding:utf-8 -*-
# __author__ = Amos
#      Email = 379833553@qq.com
#  Create_at = 2018/10/31 上午11:16
#   FileName = node_env_init

from utils.common import stop_service,get_netcard,get_gateway,FileModify,restart_service,get_shell_response,exec_shell,\
    SSHConnect,parse_address,check_is_localip,check_rsa_secret,create_rsa_secret,ssh_copy_id
import os
from config import config as CONFIG
from kubernetes.settings import settings as SETTINGS

TEMPLATE_DIR = SETTINGS.TEMPLATE_DIR
VERSION = SETTINGS.VERSION
FILES_DIR = SETTINGS.FILES_DIR
IPS = SETTINGS.IPS


# 修改网络配置
def init_network():
    # 关掉NetworkManager服务
    stop_service(['NetworkManager'])
    # 修改配置文件
    net_info = get_netcard()
    for n,ip in net_info:
        path = '/etc/sysconfig/network-scripts/ifcfg-{0}'.format(n)
        if os.path.isfile(path):
            gateway = get_gateway(n)
            f = FileModify(path)
            f.cover("""
            TYPE="Ethernet"
            BOOTPROTO=static
            IPADDR={ip}
            NETMASK=255.255.255.0
            GATEWAY={gateway}
            NM_CONTROLLED=no
            NAME={name}
            DEVICE={name}
            ONBOOT=yes
            DNS1=223.5.5.5
            """.format(name=n, ip=ip, gateway=gateway))
    # 重启服务
    restart_service(['network'])


# 关闭selinux
def close_selinux():
    resp = get_shell_response('getenforce').strip()
    if resp != 'Disabled':
        path = '/etc/selinux/config'
        f = FileModify(path)
        f.replace('(?<=SELINUX=).*', 'disabled')
        exec_shell('setenforce 0')


# 设置hostname
def set_hostname(hostname):
    exec_shell('hostname {0}'.format(hostname))
    path = '/etc/hostname'
    f = FileModify(path)
    f.cover(hostname)


# 设置hosts
def set_hosts(ip,hostname):
    path = '/etc/hosts'
    f = FileModify(path)
    f.add('{ip} {hostname}'.format(ip=ip,hostname=hostname))


# 返回K8S集群所有服务器ip
def get_all_ip(env_ip):
    if isinstance(env_ip,dict):
        ips = []
        for x in env_ip.values():
            if isinstance(x, list):
                for i in x:
                    ips.append(i)
            else:
                ips.append(x)
        return list(set(ips))
    else:
        raise ValueError('参数格式错误，请确保参数为dict格式')


# 初始化环境主函数
def init():
    ips = get_all_ip(IPS)
    scripts_dir = os.path.join(CONFIG.PROJECT_DIR, 'utils', 'scripts', 'k8s', 'init')
    for ipa in ips:
        if not check_rsa_secret():
            create_rsa_secret()
        ssh_copy_id(ipa)
        ip,port = parse_address(ipa)
        print('init {}...'.format(ip))
        if not check_is_localip(ip):
            ssh = SSHConnect(host=ip,port=int(port))
            for filename in os.listdir(scripts_dir):
                f = FileModify(os.path.join(scripts_dir, filename))
                ssh.run(f.content())
            ssh.close()
        else:
            for filename in os.listdir(scripts_dir):
                f = FileModify(os.path.join(scripts_dir, filename))
                exec_shell(f.content())


# 获取cfss可执行文件路径
def get_cfssl_dir():
    return os.path.join(FILES_DIR,VERSION,'cfssl')


# 返回etcd集群初始化地址
def get_etcd_cluster(type=str):
    etcds = IPS.get('etcd')
    ETCD_INITIAL_CLUSTER = []
    etcd_cluster_dict = {}
    for i in range(1, len(etcds) + 1):
        ip, port = parse_address(etcds[i - 1])
        ETCD_INITIAL_CLUSTER.append('etcd-node{}=https://{}:2380'.format(i, ip))
        etcd_cluster_dict[ip] = 'etcd-node{}'.format(i)
    if type == 'dict':
        return etcd_cluster_dict
    else:
        return ','.join(ETCD_INITIAL_CLUSTER)


# 返回etcd集群访问地址
def get_etcd_endpoints():
    ETCD_ENDPOINTS = []
    for i in IPS.get('etcd'):
        ip,port = parse_address(i)
        ETCD_ENDPOINTS.append('https://{}:2379'.format(ip))
    return ','.join(ETCD_ENDPOINTS)


if __name__ == '__main__':
    print(get_etcd_endpoints())