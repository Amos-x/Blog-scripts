# -*- coding:utf-8 -*-
# __author__ = Amos
#      Email = 379833553@qq.com
#  Create_at = 2018/12/20 下午4:27
#   FileName = gitlab_backup.py

from utils.common import exec_shell,SSHConnect
import time
import os
import re

# 单位秒
backup_keep_time = 86400
local_backup_dir = '/backups/gitlab'

host = '172.18.196.237'
port = 65503
remote_backup_dir = '/var/opt/gitlab/backups'

now = str(int(time.time()))[:-3]

ssh = SSHConnect(host=host,port=port)
ssh.run('/opt/gitlab/bin/gitlab-rake gitlab:backup:create')
ssh.close()

scp_cmd = 'scp -P {} {}:{}/{}* {}'.format(port,host,remote_backup_dir,now,local_backup_dir)
exec_shell('mkdir -p {}'.format(local_backup_dir))
exec_shell(scp_cmd)

for dirname in os.listdir(local_backup_dir):
    t1 = re.findall(r'(.*?)_.*', dirname)[0]
    times = int(time.time()) - int(t1)
    if times >= backup_keep_time:
        os.remove(os.path.join(local_backup_dir,dirname))
