#import urllib.request
import urllib2

service_url = "https://blockchainapi.talkehr.com/api/Allison/GetResponse?sentence="
query="How many messages for today?"
query= urllib2.quote(query)

myurl = service_url + query

print(myurl)

contents = urllib2.urlopen(myurl).read()


response = contents.decode("utf-8")

response = response.replace("%20"," ")

print(contents)
print(response)