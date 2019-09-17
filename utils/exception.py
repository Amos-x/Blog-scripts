# -*- coding:utf-8 -*-
# __author__ = Amos
#      Email = 379833553@qq.com
#  Create_at = 2019-07-12 11:21
#   FileName = exception


class GatewayConnectException(Exception):
    def __str__(self):
        return repr('Gateway connect failed')


class FIleExisted(Exception):
    def __str__(self):
        return repr('存在同名文件')
