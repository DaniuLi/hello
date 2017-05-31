#!/usr/bin/python
# -*- coding: UTF-8 -*-

import ConfigParser
import os


# 初始化默认值
includesubdir = "yes"
keepperiod = -1
filesnumber = -1

# 根据设置时间判断文件是否过期
def compare_file_time(keepperiod, file):
    time_of_last_mod = os.path.getatime(file)
    hours_between = (time.time() - time_of_last_mod) / (60*60)
    if hours_between > keepperiod:
        return True
    return False

# 清理文件
def cleanfiles(dir, includesubdir, keepperiod, filesnumber):
    print(dir, includesubdir, keepperiod, filesnumber)
    if os.path.exists(dir) == False:
        print(dir + ' is not exists!')
    elif os.path.isfile(dir):
        print(dir + ' is a file!')
    elif os.path.isdir(dir):
        print(dir + ' is a path!')
        if keepperiod > 0:
            # 删除过期文件
            print('delete files by period:' + keepperiod)
            for i in [os.sep.join([dir, v]) for v in os.listdir(dir)]:
                if compare_file_time(keepperiod, i) and (os.path.isfile(i)):
                    os.remove(i)
                    print(i+' is removed!')
        if filesnumber > 0:
            # 删除多余文件
            print('delete files by number:' + filesnumber)
            for i in os.walk(dir):
                print(i)

# 读取安装写入的配置文件入口(平台及各网元配置文件路径)
commonfilepath = './filesCleanerConfig.ini'
#commonfilepath = '/home/ngomm/config/filesCleanerConfig.ini'
if os.path.exists(commonfilepath) == False:
    print(commonfilepath+ ' is not exists!!')
else:
    pathConfig = ConfigParser.ConfigParser()
    pathConfig.readfp(open(commonfilepath))
    secs = pathConfig.sections()
    print(secs)
    for sec in secs:
        # 读取各个配置文件中的配置,放入队列等待处理
        subFilePath = pathConfig.get(sec, 'filepath')
        print(subFilePath)
        subConfig = ConfigParser.ConfigParser()
        if os.path.exists(subFilePath) == False:
            print(subFilePath+ ' is not exists!!')
        else:
            subConfig.readfp(open(subFilePath))
            subsecs = subConfig.sections()
            for subsec in subsecs:
                print(subsec)
                if subConfig.has_option(subsec, 'includesubdir'):
                    includesubdir = subConfig.get(subsec, 'includesubdir')
                    print(includesubdir)
                if subConfig.has_option(subsec, 'keepperiod'):
                    keepperiod = subConfig.get(subsec, 'keepperiod')
                    print(keepperiod)
                if subConfig.has_option(subsec, 'filesnumber'):
                    filesnumber = subConfig.get(subsec, 'filesnumber')
                    print(filesnumber)
                cleanfiles(subsec, includesubdir, keepperiod, filesnumber)
