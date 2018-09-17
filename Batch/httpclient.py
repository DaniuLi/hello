import json,urllib2

textmod = ""
print(textmod)

header_dict = {'User-Agent': 'CPE CWMP Client','Content-Type': 'text/xml; charset=utf-8','Connection': 'keep-alive'}

url='http://10.42.205.168:1234'

req = urllib2.Request(url=url,data="",headers=header_dict)
res = urllib2.urlopen(req)
res = res.read()

print(res)
