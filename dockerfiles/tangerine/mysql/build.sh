#!/usr/bin/env bash

source conf.sh
source mysql_conf.sh

#ENV_VAR=$1
#for var in ${ENV_ARR[*]}
#do
#    if [ "$ENV_VAR" != "$var" ];
#    then
#        echo "传入的第一个参数为:\"" $ENV_VAR "\" ,需要匹配下列单词: " ${ENV_ARR[*]}
#        echo "\n"
#        exit
#    fi
#done

#cat > Dockerfile << EOF
##下载mysql的镜像
#FROM mysql:5.6
##将本地文件挂到到/tmp目录
#VOLUME /tmp
#
##复制文件到容器
#ADD setup.sh /setup.sh
#
##暴露80端口
#EXPOSE 80
##配置启动容器后执行的命令
#ENTRYPOINT ["bash","/setup.sh"]
#EOF

# init 变量
product_docker_server_home=${DOCKER_VALUME}/${server}/${web_server_port}
mkdir -p ${product_docker_server_home}/{conf,data,logs}
#docker run -d --name ${docker_version}-${ENV_VAR} -p ${web_server_port}:${web_internet_port} -p  mysql:5.6


# 创建redis.conf配置文件
cat > ${product_docker_server_home}/conf/my.cnf << off
[mysqld]
user=mysql
character-set-server=utf8
[client]
default-character-set=utf8
[mysql]
default-character-set=utf8
off


docker run -p ${web_server_port}:${web_internet_port} --name ${server} -v ${product_docker_server_home}/conf:/etc/mysql -v ${product_docker_server_home}/logs:/logs -v ${product_docker_server_home}/data:/mysql_data -e MYSQL_ROOT_PASSWORD=${PASSWORD} -d $docker_version


# 安装客户端
yum install mysql -y
yum install epel-release -y
yum -y install python-pip
yum install python-devel -y
pip install --upgrade pip
pip install mycli


# Shell脚本中执行sql语句，操作mysql数据库
# https://blog.csdn.net/u011630575/article/details/50986835/

echo "mysql -h"${HOST}" -P"${PORT}" -u"${USERNAME}" -p"${PASSWORD} "-e SET PASSWORD FOR "root"@"%" = PASSWORD("oracle"); grant all privileges on *.* to ybl2018@"%" identified by "ybl2018@"; flush privileges;"

mysql -h"$HOST" -P"${PORT}" -u"$USERNAME" -p"$PASSWORD" -e '
SET PASSWORD FOR "root"@"%" = PASSWORD("oracle"); grant all privileges on *.* to ybl2018@"%" identified by "ybl2018@"; flush privileges;
'

#tee ./mysql_local_`date +%s`.log
#show variables like "%character%";
#SET PASSWORD FOR "root"@"localhost" = PASSWORD("oracle");
#grant all privileges on *.* to ybl2018@"%" identified by "ybl2018@";
#flush privileges;
#notee

cat mysql_local_*.log


# 创建命令工具
create_toolkit $server

#用本地33061端口映射docker的3306端口
#给容器命名mysql1
#用本地/home/val/docker/mysql1/conf映射mysql的conf
#用本地/home/val/docker/mysql1/logs映射mysql的logs
#用本地/home/val/docker/mysql1/data映射mysql的mysql_data

#参数说明：
#--privileged=true：容器内的root拥有真正root权限，否则容器内root只是外部普通用户权限
#-v ${productdirdata}/docker/redis/conf/redis.conf:/etc/redis/redis.conf：映射配置文件
#-v ${productdirdata}/docker/redis/data:/data：映射数据目录
# redis-server /etc/redis/redis.conf：指定配置文件启动redis-server进程
#--appendonly yes：开启数据持久化

