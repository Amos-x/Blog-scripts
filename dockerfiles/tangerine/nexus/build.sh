#!/usr/bin/env bash


# nexus
docker run -d --name nexus --restart=always -p 8081:8081  sonatype/nexus
http://112.74.48.117:8081/nexus/#welcome

admin
admin123

docker restart nexus