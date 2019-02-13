# -*- coding: utf-8 -*-

import requests
import simplejson

data = {"file_name":"sample", "path":"test","text":"Hi. I'm your virtual assistant Allison. How can I help?"}

data_json = simplejson.dumps(data)
payload = {'json_payload': data_json}

rs = requests.post("https://172.16.0.213:6010/text", json=data)

#rs = requests.post("http://localhost:6020/text", json=data)

print(rs)