from urllib import parse,request
import json


#普通数据使用::q
print('ggg 1')
textmod = parse.urlencode("").encode(encoding='utf-8')


header_dict = {'User-Agent': 'CPE CWMP Client',"Content-Type": "text/xml; charset=utf-8"}

url='http://10.42.205.168:1234'
req = request.Request(url=url,data=textmod,headers=header_dict)
res = request.urlopen(req)
res = res.read()

print('ggg 2')
print(res)
print('ggg 3')
print(res.decode(encoding='utf-8'))
