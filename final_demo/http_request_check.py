import urllib2
import requests


service_url = "https://testingapi.talkehr.com/api/Utillity/AllisonResponse?sentence="
header = {"KEY": "CASH-224-EHR-446-5002"}

query="How many messages for today"
query= urllib2.quote(query)

myurl = service_url + query

print(myurl)

r=requests.get(myurl, headers=header)
print(r)
print(r.text)

