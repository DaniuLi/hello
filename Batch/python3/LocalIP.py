#!/usr/bin/env python
#-*- coding:utf-8 -*-
 
import os
 
def get_ip():  
    #注意外围使用双引号而非单引号,并且假设默认是第一个网卡,特殊环境请适当修改代码  
    out = os.popen("ip addr | grep 'inet addr:' | grep -v '127.0.0.1' | cut -d: -f2 | awk '{print $1}' | head -1").read()  
    print (out)

if __name__ == '__main__':  
    get_ip()  