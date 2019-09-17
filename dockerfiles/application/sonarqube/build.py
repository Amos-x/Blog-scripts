# -*- coding:utf-8 -*-
# __author__ = Amos
#      Email = 379833553@qq.com
#  Create_at = 2018/11/8 下午3:48
#   FileName = build

from config import config as CONFIG
from utils.common import exec_shell,container_is_exist


def build_sonarqube():
    if not container_is_exist('sonarqube'):
        pull = 'docker pull sonarqube:7.1'
        exec_shell(pull)

        build = 'docker run -d --name sonarqube \
            -p 9000:9000 \
            -e SONARQUBE_JDBC_USERNAME={mysql_username} \
            -e SONARQUBE_JDBC_PASSWORD={mysql_password} \
            -e SONARQUBE_JDBC_URL=jdbc:mysql://{mysql_host}:3306/{soanr_db_name}?useUnicode=true\&characterEncoding=utf8\&rewriteBatchedStatements=true\&useConfigs=maxPerformance \
            sonarqube:7.1'.format(mysql_host=CONFIG.MYSQL_HOST,mysql_username=CONFIG.MYSQL_USERNAME,
                                  mysql_password=CONFIG.MYSQL_PASSWORD,soanr_db_name=CONFIG.MYSQL_NAME_SONARQUBE)

        exec_shell(build)

        exec_shell('docker start sonarqube')
    else:
        print('sonarqube 容器已存在，跳过安装')
