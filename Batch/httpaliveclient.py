import requests

client=requests.session()
headers = {'User-Agent': 'CPE CWMP Client','Content-Type': 'text/xml; charset=utf-8','Connection': 'keep-alive'}

url='http://10.42.205.170:9011'
r=client.get(url,headers=headers,data="aaaa")
print (r.status_code)
r=client.get(url,headers=headers,data="")
print (r.status_code)