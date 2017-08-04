#-*- coding:utf-8 -*-

import os
import re

from sys import argv

print ("the first variable is:", argv[0])
#print ("the second variable is:", argv[1])

with open('./a.ini','r') as r:
    lines=r.readlines()

with open('./a.ini','w') as w:
    for l in lines:
        w.write(l.replace('a','b'))