# -*- coding:utf-8 -*-
# __author__ = Amos
#      Email = 379833553@qq.com
#  Create_at = 2018/12/21 下午2:21
#   FileName = svn_back.py

from utils.common import exec_shell,SSHConnect
import time
import os
import re

# 单位秒, 86400s = 1天
backup_keep_time = 86400
local_backup_dir = '/backups/svn'

host = '172.18.196.237'
port = 65503
remote_backup_dir = '/productdir/data/backups'

now = int(time.time())

ssh = SSHConnect(host=host,port=port)
ssh.run('tar -zcf {0}/svnrepos.tar.gz {0}/../svnrepos'.format(remote_backup_dir))
ssh.close()

scp_cmd = 'scp -P {} {}:{}/svnrepos.tar.gz {}/svnrepos_{}.tar.gz'.format(port,host,remote_backup_dir,local_backup_dir,now)
exec_shell('mkdir -p {}'.format(local_backup_dir))
exec_shell(scp_cmd)

for dirname in os.listdir(local_backup_dir):
    t1 = re.findall(r'svnrepos_(.*?).tar.gz', dirname)[0]
    times = int(time.time()) - int(t1)
    if times >= backup_keep_time:
        os.remove(os.path.join(local_backup_dir,dirname))
