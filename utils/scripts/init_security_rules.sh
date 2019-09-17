#!/usr/bin/env bash


# ssh 更新
sed -i 's/#UseDNS yes/UseDNS no/g' /etc/ssh/sshd_config
sed -i 's/#GSSAPIAuthentication no/GSSAPIAuthentication no/g' /etc/ssh/sshd_config
sed -i 's/GSSAPIAuthentication yes/#GSSAPIAuthentication yes/g' /etc/ssh/sshd_config
service sshd restart

# 密码长度
sed -i 's/^PASS_MIN_LEN *[1-9]$/PASS_MIN_LEN    8/g' /etc/login.defs

# 关闭 selinux
sed -i 's/^SELINUX=[a-z]*$/SELINUX=disabled/g' /etc/selinux/config