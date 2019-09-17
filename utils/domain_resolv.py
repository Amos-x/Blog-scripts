# -*- coding:utf-8 -*-
# __author__ = Amos
#      Email = 379833553@qq.com
#  Create_at = 2019-05-24 10:29
#   FileName = domain_resolv

from dns import resolver
import re
import os
import smtplib
from email.mime.text import MIMEText
from email.header import Header


def get_ip(domain):
    try:
        A = resolver.query(domain,'A')
        ips = []
        for i in A.response.answer:
            for j in i:
                ips.append(j.address)
        return ips
    except:
        return None


def alter_hosts(ip, host):
    hosts_path = '/etc/hosts'
    f = FileModify(hosts_path)
    f.replace('.*?{}'.format(host), '{} {}'.format(ip, host))


# 操作文件
class FileModify(object):
    def __init__(self, file_path, autocreate=False):
        self.file_path = file_path
        self._autocreate = autocreate
        self.check_exists()

    # 检查文件是否存在，不存在则报错或自动创建文件
    def check_exists(self):
        if not os.path.exists(self.file_path):
            if not self._autocreate:
                raise ValueError('文件不存在，请检查路径')
            else:
                with open(self.file_path, 'w', encoding='utf-8') as f:
                    pass

    # 添加到文件末尾
    def add(self, context):
        with open(self.file_path, 'a', encoding='utf-8') as f:
            f.write(context + '\n')

    # 修改替换文件内容，old支持正则匹配
    def replace(self, old, new, line_num=None):
        with open(self.file_path, 'r+', encoding='utf-8') as f:
            ff = f.readlines()
            if line_num:
                ff[line_num] = re.sub(old, new, ff[line_num])
            else:
                for line in range(len(ff)):
                    ff[line] = re.sub(old, new, ff[line])

        with open(self.file_path, 'w', encoding='utf-8') as f2:
            f2.writelines(ff)

    # 重写覆盖整个文件
    def cover(self, context):
        with open(self.file_path, 'w', encoding='utf-8') as f:
            f.write(context)

    # 获取文件内容
    def content(self):
        with open(self.file_path, 'r', encoding='utf-8') as f:
            return f.read()


def send_mail():
    HOST = "smtp.163.com"
    PORT = "465"
    USER = '18814184409@163.com'
    PASSWD = 'wyx379833553'
    TO = '379833553@qq.com'

    smtp = smtplib.SMTP_SSL(HOST, PORT)
    smtp.login(USER, PASSWD)

    message = MIMEText('Graylog日志收集到hdfs的dns解析不到了，尽快解决', 'plain', 'utf-8')
    message['From'] = USER
    message['To'] = TO
    message['Subject'] = Header('严重错误，尽快解决', 'utf-8')

    smtp.sendmail(USER, TO, message.as_string())
    smtp.quit()


if __name__ == '__main__':
    Domain = '2x140809f2.iask.in'
    host = 'ybl'
    ips = get_ip(Domain)
    if ips:
        alter_hosts(ips[0], host)
        print('ok')
    else:
        send_mail()
