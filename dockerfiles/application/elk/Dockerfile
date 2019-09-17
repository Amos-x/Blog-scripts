# Base Image
FROM sebp/elkx:624

# Maintainer
MAINTAINER Amos wangyx@yaobili.com

# logstash 配置
COPY 02-beats-input.conf /etc/logstash/conf.d/
COPY 30-output.conf /etc/logstash/conf.d/

EXPOSE 5046
