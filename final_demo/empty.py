how many messages for today
ho is my first patient for today
who is my next patient
how many appointment do i have for today
when was last time patient was immunized 
when was next well visit due for this patient
any status update


import requests
import simplejson

data = {"file_name":"unable", "path":"test","text":"Sorry, I couldnt understand what you said."}

data_json = simplejson.dumps(data)
payload = {'json_payload': data_json}

rs = requests.post("http://172.16.0.213:6020/text", json=data)
