# -*- coding:utf-8 -*-
# __author__ = Amos
#      Email = 379833553@qq.com
#  Create_at = 2018/12/21 上午11:30
#   FileName = source_back.py

from utils.common import SSHConnect,exec_shell
import time
import os
import re
import datetime

# 备份保留时间，单位：天
backup_keep_time = 2

host = '172.18.196.243'
port = 22
remote_backup_dir = '/mnt/wwwroot/history_version'

local_backup_dir = '/backups/static'

ssh = SSHConnect(host=host,port=port)
ssh.run('tar -zcf {}/source.tar.gz /mnt/wwwroot/source'.format(remote_backup_dir))
ssh.close()
today = time.strftime('%Y%m%d',time.localtime(time.time()))
exec_shell('mkdir -p /backups/static')
scp_cmd = 'scp {}:{}/source.tar.gz {}/source_{}.tar.gz'.format(host,remote_backup_dir,local_backup_dir,today)
exec_shell(scp_cmd)

for dirname in os.listdir(local_backup_dir):
    t1 = re.findall(r'source_(.+?).tar.gz', dirname)[0]
    time1 = datetime.datetime.strptime(t1, '%Y%m%d')
    time_dif = datetime.datetime.today() - time1
    times = time_dif.days
    if times >= backup_keep_time:
        os.remove(os.path.join(local_backup_dir,dirname))
