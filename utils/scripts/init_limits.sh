#!/usr/bin/env bash

# 资源限制
cat >> /etc/security/limits.conf << EOF
root soft nofile 65535
root hard nofile 65535
* soft nofile 65535
* hard nofile 65535
EOF

