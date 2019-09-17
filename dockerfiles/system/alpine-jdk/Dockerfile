FROM alpine:latest
ADD server-jre-8u201-linux-x64.tar.gz /usr/local

RUN apk --no-cache add ca-certificates wget && \
    wget -q -O /etc/apk/keys/sgerrand.rsa.pub https://alpine-pkgs.sgerrand.com/sgerrand.rsa.pub && \
    wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.28-r0/glibc-2.28-r0.apk && \
    apk add glibc-2.28-r0.apk


RUN sed -i 's/#crypto.policy=unlimited/crypto.policy=unlimited/' /usr/local/jdk1.8.0_201/jre/lib/security/java.security
RUN rm -Rf COPYRIGHT LICENSE README.html THIRDPARTYLICENSEREADME-JAVAFX.txt THIRDPARTYLICENSEREADME.txt release src.zip man/

# 时区设置
RUN apk add -U tzdata
RUN cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime

ENV JAVA_HOME=/usr/local/jdk1.8.0_201
ENV JRE_HOME=$JAVA_HOME/jre
ENV CLASSPATH=$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar:$JRE_HOME/lib/dt.jar
ENV PATH=.:$JAVA_HOME/bin:$JRE_HOME/bin:$PATH
CMD ["java","-version"]