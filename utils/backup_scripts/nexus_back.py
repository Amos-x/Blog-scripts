# -*- coding:utf-8 -*-
# __author__ = Amos
#      Email = 379833553@qq.com
#  Create_at = 2018/12/21 下午2:42
#   FileName = nexus_back.py

from utils.common import exec_shell,SSHConnect
import time
import os
import re


# 单位秒, 86400s = 1天
backup_keep_time = 86400 * 3
local_host = '172.18.73.128'
local_backup_dir = '/backups/nexus'

host = '172.18.73.129'
port = 65503
remote_backup_dir = '/backups/nexus'
dir = '/var/lib/docker/volumes/bd01a4f32e58cc69a3ad888c6c621a37a72b43e3e964352117d30e112fb5a931/_data/storage'

now = int(time.time())

ssh = SSHConnect(host=host,port=port,password='ybl2018nb@')
ssh.run('mkdir -p {}'.format(remote_backup_dir))
ssh.run('tar -zcf {}/nexus.tar.gz {}'.format(remote_backup_dir,dir))
scp_cmd = 'scp -P {} {}/nexus.tar.gz {}:{}/nexus_{}.tar.gz'.format(port,remote_backup_dir,local_host,local_backup_dir,now)
ssh.run(scp_cmd)
ssh.run('rm -rf {}'.format(remote_backup_dir))
ssh.close()

exec_shell('mkdir -p {}'.format(local_backup_dir))

for dirname in os.listdir(local_backup_dir):
    t1 = re.findall(r'nexus_(.*?).tar.gz', dirname)[0]
    times = int(time.time()) - int(t1)
    if times >= backup_keep_time:
        os.remove(os.path.join(local_backup_dir,dirname))
