#!/bin/bash
# __author__ = Amos
#      Email = 379833553@qq.com
#  Create_at = 2018/11/16 上午11:52
#   FileName = ${NAME}

mkdir -p /opt/kubernetes/{cfg,bin,ssl,log}
result=`grep -nr /opt/kubernetes/bin /etc/profile`

if [ ! -n "$result" ]; then
cat >> /etc/profile <<EOF

# kubernetes env
export PATH=\$PATH:/opt/kubernetes/bin
EOF
source /etc/profile
fi
