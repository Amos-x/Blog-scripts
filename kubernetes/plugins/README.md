
# kubernetes 插件集

插件列表：
```
* coredns
* dashboard
* helm
* metrics-server
* prometheus-operator
* treafik-ingress
```

安全密钥文件 
```
* secrets
```

<br>

##使用介绍

#### Coredns
> k8s集群必要基础插件DNS的一种，最好用和使用人数最多的有：
> 官方:     kubedns \
> 第三方：  coredns \
> 这里用的第三方coredns

```angular2html
kubectl apply -f plugins/coredns/coredns.yaml
```

<br>

#### Dashboard
> k8s集群官方web界面，分为with_ssl和no_ssl，为方便配置，这里使用no_ssl部署dashboard

```angular2html
# 创建静态认证文件，用户密码
# htpasswd -bc kubernetes-dashboard-auth username password

# 创建对应secret，用于静态认证登陆认证
kubectl create secret generic kubernetes-dashboard-basic-auth --from-file=kubernetes-dashboard-auth --namespace=kube-system

# 部署yaml文件
kubectl apply -f plugins/dashboard/no_ssl/
```

<br>

#### Helm
> 使用时，直接执行build.sh脚本，自动安装kubernetes集群的helm插件

```angular2html
sh plugins/helm/build.sh
```

<br>

#### Metrics-server
> metrics-server是新版k8s集群的监控数据采集插件，替代原本的heapster插件。使用集群内节点的状态监控。并可以根据状态进行动态扩缩容

```angular2html
kubectl apply -f plugins/metrics-server/
```

<br>

#### Traefik-ingress
> ingress是k8s集群提供外部访问的一种负载均衡方式，常用的有nginx和treafik。
> treafik凭借其轻量，快速，配置的自动修改等等好处成为最受欢迎的方案

```angular2html
# treafik 使用daemonset来部署，所有需要提前设置节点的标签，通过标签选择指定部署的节点。
# 给节点打标签
kubectl label nodes node-name traefik=yes

# 创建treafik的ui认证secret
kubectl create secret generic traefik-ui-basic-auth --from-file=treafik-ui-auth --namespace=kube-system

# 部署treafik
kubectl apply -f plugins/treafik-ingress/

```

<br>

#### Secrets
> secrets 是k8s集群中的密钥认证配置，所有使用到的认证都需要提前将之加入secrets中
> 在需要用到时，直接指定secret的名字来引用

这里演示配置镜像仓库的认证，如阿里云或harbor等
```angular2html
# 创建secret有两种方法：
1 - 命令行直接创建

kubectl create secret docker-registry registry-secret --namespace=default \
--docker-server=https://private-registry.domain.com --docker-username=username \
--docker-password=password --docker-email=username@abcd.com

2 - 登陆后，使用配置信息转码，写yaml文件创建
# 登陆镜像仓库
docker login registry-server-addr

# 将生产的配置进行base64编码，然后见编码后的字符串复制到yaml文件中
cat ~/.docker/config.json | base64 -w 0

# yaml文件见 plugins/secrets/harbor-secret.yaml，替换其中.dockerconfigjson的数据

```

<br>

#### Prometheus-operator
> 普罗米修斯监控服务，可以全方位的监控kubernetes集群，并提供报警功能，通过grfana来实现可视化面板，是k8s集群中最主要的监控解决方案

```angular2html
# 首先，部署普罗米修斯
kubectl apply -f plugins/prometheus-operator/manifests/

# 创建认证secret
kubectl create secret generic prometheus-web-auth --from-file=prometheus-web-auth --namespace=monitoring

# 部署访问的ingress和email配置
kubectl apply -f plugins/prometheus-operator/

```
