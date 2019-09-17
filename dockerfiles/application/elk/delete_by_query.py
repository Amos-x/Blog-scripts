# -*- coding:utf-8 -*-
# __author__ = Amos
#      Email = 379833553@qq.com
#  Create_at = 2019/1/3 11:20 AM
#   FileName = delete_by_query

import requests
import json

es_host = 'test.elk.yaobili.com'

headers = {
    'Content-Type': 'application/json'
}

url = 'http://{}:9200/*/_delete_by_query?conflicts=proceed'.format(es_host)

data = {
    "query": {
        "range": {
            "@timestamp": {
                "lt": "now-7d",
                "format": "epoch_millis"
            }
        }
    }
}

response = requests.post(url, headers=headers, data=json.dumps(data))
print(response.json())

url2 ='http://{}:9200/_forcemerge?only_expunge_deletes=true&max_num_segments=1'.format(es_host)
response = requests.post(url2)

print(response.json())
