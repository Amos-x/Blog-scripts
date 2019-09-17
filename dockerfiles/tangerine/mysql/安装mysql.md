
#创建目录
cd / 
mkdir /productdir/docker
mkdir /productdir/docker/mysql 
cd /productdir/docker/mysql 
mkdir config 
mkdir db
chown -R vagrant. /productdir/docker

// 忽略容器的权限管理
--privileged=true

docker run -d -p 3306:3306 --name mysql01 -v=/productdir/docker/mysql/config/my.cnf:/etc/my.cnf -v=/productdir/docker/mysql/data:/var/lib/mysql   --privileged=true  mysql/mysql-server 


sudo docker run --name mysql_server -d --restart always -p 3306:3306 -e MYSQL_ROOT_PASSWORD=oracle -v /docker/mysql/data:/var/lib/mysql mysql/mysql-server

# 登录
docker exec -it imooc-mysql bash 


# ERROR 2059 (HY000): Authentication plugin 'caching_sha2_password' cannot be loaded: /usr/lib64/mysql/plugin/caching_sha2_password.so: cannot open shared object file: No such file or directory

# 2018-10-05T13:34:10.950655Z 0 [ERROR] [MY-010123] [Server] Fatal error: Please read "Security"
section of the manual to find out how to run mysqld as root!





输入docker ps查看，已经运行了mysql01容器，继续以下操作

查看日志，找到初始密码，
docker logs mysql01

进入容器 : 
docker exec -it mysql01 bash 

使用root登录mysql : 
mysql -u root -p，
然后输入刚才日志中找到的密码，进入mysql。 
设置密码：
SET PASSWORD FOR 'root'@'localhost' = PASSWORD('oracle');


# 8.0版本 使用下面初始化命令
alter user user() identified by "oracle";

CREATE USER 'tangerine'@'%' IDENTIFIED BY 'oracle';
GRANT ALL PRIVILEGES ON *.* TO 'tangerine'@'%' WITH GRANT OPTION;
# 需要加上这一句不然不能访问容器
ALTER USER 'tangerine'@'%' IDENTIFIED WITH mysql_native_password BY 'oracle';
flush privileges;



