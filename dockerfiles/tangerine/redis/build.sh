#!/usr/bin/env bash
#docker run --name redis -d -p 6379:6379 redis --requirepass "admin"
#docker run --name redis -d -p 6379:6379 redis

source conf.sh

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


#普通安装
#1.拉取镜像，redis:4.0
# docker pull redis:4.0


#2.创建redis容器名"redistest1"，并开启持久化
#docker run -d -p 6379:6379 --name redistest1 redis:4.0 redis-server --appendonly yes

#参数说明：
# --appendonly yes：开启持久化

#挂载外部配置和数据安装
# 1.创建目录和配置文件redis.conf


product_docker_server_home=${DOCKER_VALUME}/${server}/${server_port}
chmod -R 777 ${DOCKER_VALUME}/${server}
mkdir -p ${product_docker_server_home}/conf
mkdir -p ${product_docker_server_home}/data

#创建redis.conf配置文件
cat > ${product_docker_server_home}/conf/redis.conf << off
#daemonize yes
port ${server_port}
pidfile /data/redis.pid
dir /data

loglevel notice
logfile /data/${server_port}.log

tcp-backlog 511
timeout 0
tcp-keepalive 0
databases 16
# requirepass 4239822ca2cc969d020c57208652b8fe
maxmemory 512M

save 900 1
save 300 10
save 60 10000

rdbcompression no
rdbchecksum yes
stop-writes-on-bgsave-error yes
dbfilename ${server_port}.rdb

appendonly yes
appendfilename "${server_port}.aof"
appendfsync everysec

no-appendfsync-on-rewrite no
auto-aof-rewrite-percentage 100
auto-aof-rewrite-min-size 64mb
aof-load-truncated yes

lua-time-limit 5000
slowlog-log-slower-than 10000
slowlog-max-len 128

latency-monitor-threshold 0
notify-keyspace-events ""

hash-max-ziplist-entries 512
hash-max-ziplist-value 64
list-max-ziplist-entries 512
list-max-ziplist-value 64
set-max-intset-entries 512
zset-max-ziplist-entries 128
zset-max-ziplist-value 64
hll-sparse-max-bytes 3000

activerehashing yes

client-output-buffer-limit normal 0 0 0
client-output-buffer-limit slave 256mb 64mb 60
client-output-buffer-limit pubsub 32mb 8mb 60
hz 10

aof-rewrite-incremental-fsync yes

slave-serve-stale-data yes
repl-diskless-sync no
repl-diskless-sync-delay 5
repl-disable-tcp-nodelay no
slave-read-only yes
slave-priority 100

# daemonize yes
off

#redis.conf文件内容自行添加：
#切记注释掉：#daemonize yes 否则无法启动容器
#重要话说三遍：注释掉#daemonize yes，注释掉#daemonize yes，注释掉#daemonize yes
## 2.创建启动容器，加载配置文件并持久化数据

#docker run -d --privileged=true -p 6379:6379 -v /docker/redis/conf/redis.conf:/etc/redis/redis.conf -v /docker/redis/data:/data --name redistest2 redis:4.0 redis-server /etc/redis/redis.conf --appendonly yes


docker run -d --privileged=true -p ${internet_port}:${server_port} -v ${product_docker_server_home}/conf/redis.conf:/etc/redis/redis.conf -v ${product_docker_server_home}/data:/data --name ${docker_container_name} redis:3.2 redis-server /etc/redis/redis.conf --appendonly yes

# --privileged=true

#参数说明：
#--privileged=true：容器内的root拥有真正root权限，否则容器内root只是外部普通用户权限
#-v ${productdirdata}/docker/redis/conf/redis.conf:/etc/redis/redis.conf：映射配置文件
#-v ${productdirdata}/docker/redis/data:/data：映射数据目录
#redis-server /etc/redis/redis.conf：指定配置文件启动redis-server进程
#--appendonly yes：开启数据持久化


# 创建命令工具
create_single_toolkit $server

