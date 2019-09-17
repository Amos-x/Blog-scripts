# Base Image
FROM centos:7.4.1708

# Maintainer
MAINTAINER Amos wangyx@yaobili.com

# Run
RUN rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7
RUN rpm -ivh https://mirrors.aliyun.com/epel/epel-release-latest-7.noarch.rpm  && yum clean all && yum makecache
RUN yum install -y python36 python36-setuptools && easy_install-3.6 pip
RUN yum clean all && rm -rf /var/cache/yum/*

CMD ["/bin/bash"]
