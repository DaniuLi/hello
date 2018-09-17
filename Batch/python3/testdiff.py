#-*- coding: UTF-8 -*-
import re
import sys
import os

import sys
import difflib
 
a = open('a.txt', 'U').readlines()
b = open('b.txt', 'U').readlines()
diff = difflib.ndiff(a, b)
 
#sys.stdout.writelines(diff)

#print(list(diff))


def dedupe(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)

str1=[]
str2=[]
str_dump=[]
fa=open("a.txt",'r')
fb=open("b.txt",'r')
fc=open("c.txt",'w+')
 
#将A.txt的内容逐行读到str1中
for line in fa.readlines():
    str1.append(line.replace("\n",''))
#将B.txt中的内容逐行读到str2中
for line in fb.readlines():
    str2.append(line.replace("\n",''))
 
#将两个文件中重复的行，添加到str_dump中
#for i in str1:
#    if i in str2:
#        str_dump.append(i)
 
#将两个文件的行合并，并去重
#str_all=set(str1+str2)
str_rslt=str2


#将重复的行，在去重的合并行中，remove掉，剩下的就是不重复的行了
#for i in str_dump:
for i in str1:
    if i in str2:
        str_rslt.remove(i)
#写行文件中
for i in list(str_rslt):
    fc.write(i+'\n')
 
fa.close()
fb.close()
fc.close()