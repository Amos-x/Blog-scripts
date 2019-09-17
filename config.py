# -*- coding:utf-8 -*-
# __author__ = Amos
#      Email = 379833553@qq.com
#  Create_at = 2018/11/5 上午3:01
#   FileName = config

# __author__ = "Amos"
# Email: 379833553@qq.com
"""
    config.py
    ~~~~~~~~~~~~~~~~~

    Work_Script project setting file

"""
import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)


class Config:
    PROJECT_DIR = BASE_DIR

    # Harbor 仓库的一些配置，用于image的构建与拉取等
    # harbor 的域名
    HARBOR_DOMAIN = "harbor.yaobili.com"
    # harbor 的项目，用于选择将镜像上传到指定项目
    HARBOR_PROJECTS = ["base-env", "apps"]

    # k8s 相关配置
    # 环境配置TE,ST是本地虚拟服务器环境，PROD为阿里云正式环境，默认为TEST
    ENV = "test"

    K8S_TEST_ENV = {
        "master": ["172.18.196.238:65503"],
        "nodes": ["172.18.249.10", "172.18.46.103", "172.18.73.132"],
        "etcd": ["172.18.196.238:65503","172.18.249.10","172.18.73.132"]
    }
    K8s_PROD_ENV = {
        "master": ["172.18.46.101"],
        "nodes": ["172.18.249.8", "172.18.249.9", "172.18.46.102", "172.18.73.136", "172.18.73.137"],
        "etcd": ["172.18.249.8", "172.18.249.9", "172.18.46.102", "172.18.73.136", "172.18.73.137"]
    }

    # mysql 相关配置, 使用阿里云数据库
    MYSQL_HOST = "rm-wz9xqe04o3v4y20sj.mysql.rds.aliyuncs.com"
    MYSQL_USERNAME = "ybl2018"
    MYSQL_PASSWORD = "ybl2018@"

    # sonarqube 数据库名
    MYSQL_NAME_SONARQUBE = "sonar"
    # jumpserver 数据库名
    MYSQL_NAME_JUMPSERVER = "jumpserver"

    def __init__(self):
        pass

    def __getattr__(self, item):
        return None


class DevelopmentConfig(Config):
    pass


class ProductionConfig(Config):
    pass


# # Default using Config settings, you can write if/else for different env
config = DevelopmentConfig()

