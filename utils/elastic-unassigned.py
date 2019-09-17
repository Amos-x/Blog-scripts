# -*- coding:utf-8 -*-
# __author__ = Amos
#      Email = 379833553@qq.com
#  Create_at = 2019-05-20 17:23
#   FileName = elastic-unassigned

import requests
import json

elastic_ip = 'localhost'

# 查看分片
url = 'http://{}:9200/_cat/shards'.format(elastic_ip)
response = requests.get(url)
print(response.content)

# 查看节点信息
url2 = 'http://{}:9200/_nodes/process?pretty'.format(elastic_ip)
response = requests.get(url2)
print(response.content)

# 重设分片
url3 = 'http://{}:9200/_cluster/reroute'.format(elastic_ip)
headers = {'Content-Type': 'application/json'}
data = {
    "commands": [
        {
            "allocate_replica": {
                "index": "user_info",
                "shard": 0,
                "node": "2Yk8bN5OQkmiRrSNhADxMg",
                "allow_primary": "true"
            }
        }
    ]
}
response = requests.post(url3, headers=headers, data=json.dumps(data))
print(response.status_code)
print(response.content)

# 删除分片
url4 = 'http://{ip}:9200/{index_name}'.format(ip=elastic_ip, index_name='index_name')
response = requests.delete(url4)
print(response.content)


requests.post(url,data=json.dumps())
response.status_code