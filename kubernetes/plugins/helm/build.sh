#!/bin/bash
# __author__ = Amos
#      Email = 379833553@qq.com
#  Create_at = 2019/1/4 7:04 PM

# 安装helm
cd /usr/local/src
wget https://storage.googleapis.com/kubernetes-helm/helm-v2.12.1-linux-amd64.tar.gz
tar zxf helm-v2.12.1-linux-amd64.tar.gz
mv linux-amd64/helm /opt/kubernetes/bin/

# 通过helm安装tiller
helm init --upgrade -i registry.cn-hangzhou.aliyuncs.com/google_containers/tiller:v2.12.1 --stable-repo-url https://kubernetes.oss-cn-hangzhou.aliyuncs.com/charts

# 每个节点都需要安装
yum install -y socat

# RBAC授权
kubectl create serviceaccount --namespace kube-system tiller
kubectl create clusterrolebinding tiller-cluster-rule --clusterrole=cluster-admin --serviceaccount=kube-system:tiller
kubectl patch deploy --namespace kube-system tiller-deploy -p '{"spec":{"template":{"spec":{"serviceAccount":"tiller"}}}}'
