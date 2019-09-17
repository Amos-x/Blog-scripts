#! /usr/bin/python36
# -*- coding:utf-8 -*-
# __author__ = Amos
#      Email = 379833553@qq.com
#  Create_at = 2018/12/4 下午6:02
#   FileName = build

from config import config as CONFIG
import argparse
from kubernetes.util import init
from kubernetes.modules.ca import build as ca_build
from kubernetes.modules.etcd import build as etcd_build
from kubernetes.modules.etcd import check_health

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="""
    Example:
    %(prog)s service init
    """)
    parser.add_argument('service',type=str, choices=['k8s'],help='select service to build')
    parser.add_argument('action', type=str, choices=['init','install','check'], default='install', nargs='?',
                        help='select action to run, default is install')
    parser.add_argument('-e', '--env', choices=['test','prod'], type=str, default='test',help='指定环境，默认为test')

    args = parser.parse_args()

    if args.service == 'k8s':
        if args.action == 'init':
            init()
        elif args.action == 'install':
            init()
            ca_build()
            etcd_build()
        elif args.action == 'check':
            check_health()