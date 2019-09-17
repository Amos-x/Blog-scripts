#! /usr/bin/python36

import os
import re
import datetime
import subprocess

mysql_host = {
    'test': 'rm-wz9xqe04o3v4y20sj.mysql.rds.aliyuncs.com',
    'pre': 'rm-wz9uvgfjc5510w41k.mysql.rds.aliyuncs.com',
    'prod': 'rr-wz9y1fuvg1y3368qa.mysql.rds.aliyuncs.com'
}
db_user = 'ybl2018'
db_passwd = 'ybl2018@'

back_dir = '/usr/local/mysql_backup/mysqldata'

#  备份文件保存时间，单位：天
backup_keep_time = 10

ignore_database = ['Database','information_schema','mysql','performance_schema']

today = datetime.datetime.today().strftime('%Y%m%d')
for env in mysql_host:
    cmd = '/usr/bin/mysql -h {} -u{} -p{} -e "show databases"'.format(mysql_host.get(env),db_user,db_passwd)
    result = subprocess.check_output(cmd,shell=True,universal_newlines=True).split('\n')
    databases = [i for i in result if i and i not in ignore_database]
    env_backup_dir = os.path.join(back_dir,env)
    os.system('mkdir -p {}'.format(env_backup_dir))

    for database in databases:
        back_path = os.path.join(env_backup_dir,'%s_%s.sql.gz' %(database,today))
        command = '/usr/bin/mysqldump -h {} -u{} -p{} {} --fore |gzip > {}'.format(
            mysql_host.get(env),db_user,db_passwd,database,back_path
        )
        os.system(command)

    for dirname in os.listdir(env_backup_dir):
        t1 = re.findall(r'_([\d]*?).sql.gz',dirname)[0]
        time1 = datetime.datetime.strptime(t1,'%Y%m%d')
        time_dif = datetime.datetime.today()-time1
        times = time_dif.days
        if times >= backup_keep_time:
            os.remove(os.path.join(env_backup_dir,dirname))
