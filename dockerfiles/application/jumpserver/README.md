## Jumpserver

**jumpserver 构建镜像已上传至harbor仓库，请直接下载镜像使用
除非需要重新安装全新的jumpserver，否则不建议自行构建镜像``**

``harbor.yaobili.com/apps/jumpserver:latest``

&nbsp;
#### 使用说明
```angular2html
docker pull harbor.yaobili.com/apps/jumpserver:latest

docker run -d --name jumpserver -p 8000:80 -p 2222:2222 harbor.yaobili.com/apps/jumpserver:latest

```

######TIP: 数据库使用阿里云数据库实例，已在镜像中指定。


## 自行构建镜像
若从新构建镜像，需要修改Dockerfile中的数据库配置，默认配置如下：

* DB_ENGINE = mysql
* DB_HOST = mysql_host
* DB_PORT = 3306
* DB_USER = jumpserver
* DB_PASSWORD = weakPassword
* DB_NAME = jumpserver
* REDIS_HOST = 127.0.0.1
* REDIS_PORT = 6379
* REDIS_PASSWORD =

```angular2html
docker run --name jumpserver -d \
    -p 80:80 \
    -p 2222:2222 \
    -e DB_ENGINE=mysql \
    -e DB_HOST=192.168.x.x \
    -e DB_PORT=3306 \
    -e DB_USER=root \
    -e DB_PASSWORD=xxx \
    -e DB_NAME=jumpserver \
    -e REDIS_HOST=192.168.x.x \
    -e REDIS_PORT=6379 \
    -e REDIS_PASSWORD=xxx \
    yourimagesname:latest 
```
