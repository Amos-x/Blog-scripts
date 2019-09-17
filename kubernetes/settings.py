# -*- coding:utf-8 -*-
# __author__ = Amos
#      Email = 379833553@qq.com
#  Create_at = 2018/12/5 下午5:01
#   FileName = settings
"""
    settings.py
    ~~~~~~~~~~~~~~~~~

    kubernetest install settings

"""
from config import config as CONFIG
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if CONFIG.ENV == 'test':
    IPS = CONFIG.K8S_TEST_ENV
elif CONFIG.ENV == 'prod':
    IPS = CONFIG.K8s_PROD_ENV
else:
    raise ValueError('ENV参数无法识别，只支持test，prod参数')


class Settings:
    # 设置kubernetes 版本
    VERSION = '1.12'

    # 设置模版配置文件路径
    TEMPLATE_DIR = os.path.join(BASE_DIR,'template')

    # 设置软件文件目录
    FILES_DIR = os.path.join(BASE_DIR,'files')

    # 设置IPS
    IPS = IPS

    # 设置Master的IP地址(必须修改)
    MASTER_IP = IPS.get('master')

    # 设置Node节点的IP地址
    NODES_IP = IPS.get('nodes')

    # 设置ETCD集群的IP地址
    ETCD_CLUSTER_IP = IPS.get('etcd')

    # 设置ETCD集群访问地址（必须修改）
    ETCD_ENDPOINTS = "https://192.168.56.11:2379,https://192.168.56.12:2379,https://192.168.56.13:2379"

    # 设置ETCD集群初始化列表（必须修改）
    ETCD_CLUSTER = "etcd-node1=https://192.168.56.11:2380,etcd-node2=https://192.168.56.12:2380,etcd-node3=https://192.168.56.13:2380"

    # 通过Grains FQDN自动获取本机IP地址，请注意保证主机名解析到本机IP地址
    # NODE_IP =

    # 设置BOOTSTARP的TOKEN，可以自己生成
    BOOTSTRAP_TOKEN = "16efd754307d33fe6835fce45d52d6b7"

    # 配置Service IP地址段
    SERVICE_CIDR = "10.1.0.0/16"

    # Kubernetes服务 IP (从 SERVICE_CIDR 中预分配)
    CLUSTER_KUBERNETES_SVC_IP = "10.1.0.1"

    # Kubernetes DNS 服务 IP (从 SERVICE_CIDR 中预分配)
    CLUSTER_DNS_SVC_IP = "10.1.0.2"

    # 设置Node Port的端口范围
    NODE_PORT_RANGE = "20000-40000"

    # 设置POD的IP地址段
    POD_CIDR = "10.2.0.0/16"

    # 设置集群的DNS域名
    CLUSTER_DNS_DOMAIN = "cluster.local."

    # 设置Docker Registry地址
    DOCKER_REGISTRY = "http://192.168.56.11:5000"

    def __init__(self):
        pass

    def __getattr__(self, item):
        return None


class DevelopmentSettings(Settings):
    pass


class ProductionSettings(Settings):
    pass


# # Default using Config settings, you can write if/else for different env
settings = DevelopmentSettings()
