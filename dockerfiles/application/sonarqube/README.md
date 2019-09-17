# SonarQube

直接拉取官方镜像使用：`sonarqube:7.1`

详情可查看镜像地址：<https://hub.docker.com/r/library/sonarqube/>

&nbsp;

###运行镜像
```angular2html
docker run -d --name sonarqube \
    -p 9000:9000 \
    -e SONARQUBE_JDBC_USERNAME=sonar \
    -e SONARQUBE_JDBC_PASSWORD=sonar \
    -e SONARQUBE_JDBC_URL=jdbc:mysql://<mysqlhost>:3306/sonar?useUnicode=true\&characterEncoding=utf8\&rewriteBatchedStatements=true\&useConfigs=maxPerformance \
    sonarqube:7.1
```

***Tip: 在给jdbc_url参数时 "&" 符号在docker命令行中需要在前面添加 "\\" 进行转义。如：`\&`***