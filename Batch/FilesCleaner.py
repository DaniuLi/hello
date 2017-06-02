#!/usr/bin/python
# -*- coding: UTF-8 -*-

import ConfigParser
import os
import schedule
import time
import glob



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

def cleanjob():
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
                    # 初始化默认值
                    includesubdir = "yes"
                    keepperiod = -1
                    filesnumber = -1
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

#def job():
cleanjob()
print("I'm worked...")

#schedule.every(10).minutes.do(job)
#schedule.every().hour.do(job)
#schedule.every().day.at("09:10").do(job)
#schedule.every().monday.do(job)
#schedule.every().wednesday.at("13:15").do(job)

#while True:
#    schedule.run_pending()
#    time.sleep(1)

def traverseDirByOSWalk(path):
    file_dic = {}
    path = os.path.expanduser(path)
    for (dirname, subdir, subfile) in os.walk(path):
        #print('dirname is %s, subdir is %s, subfile is %s' % (dirname, subdir, subfile))
        #print('[' + dirname + ']')
        for f in subfile:
            #print(os.path.join(dirname, f))
            stats = os.stat(os.path.join(dirname, f))
            file_dic[os.path.join(dirname, f)] = stats.st_ctime

    file_list = sorted(file_dic.items(), lambda x, y: cmp(x[1], y[1]), reverse=True)
    for item in file_list:
        line = "Name: {:<20} | Date Created: {:>20}".format(item[0], time.ctime(item[1]))
        print(line)

file_list = traverseDirByOSWalk("C:/workspace/hello")





#def file_info(directory,sortLastModifiedOrNaw=False):
#    file_list = []
#    currentMin = 0 #This is the variable that will track the lowest digit
#    for i in os.listdir(directory):
#        a = os.stat(os.path.join(directory,i))
#        if sortLastModifiedOrNaw == True: #If you would like to sort.
#            if a.st_atime > currentMin: #Check if this is bigger than the current minimum. 
#                currentMin = a.st_atime #If it is we update the current minimum
#                #Below we append so that it ends up in the end of the list
#                file_list.append([i,time.ctime(a.st_atime),time.ctime(a.st_ctime)]) #[file,most_recent_access,created]
#            else: #If it is smaller, it should be in the front of the list so we insert it into position 0. 
#                file_list.insert(0,[i,time.ctime(a.st_atime),time.ctime(a.st_ctime)]) #[file,most_recent_access,created]
#        else: #If you would not like to sort
#            file_list.append([i,time.ctime(a.st_atime),time.ctime(a.st_ctime)]) #[file,most_recent_access,created]
#    return file_list


#file_list = file_info("C:/workspace/hello/BATCH")


#print("Unsorted Example")
#for item in file_list:
#    line = "Name: {:<20} | Date Last Accessed: {:>20} | Date Created: {:>20}".format(item[0],item[1],item[2])
#    print(line)

#print("\nSorted example using last modified time")
#file_list = file_info("C:/workspace/hello/BATCH",sortLastModifiedOrNaw=True)

#for item in file_list:
#    line = "Name: {:<20} | Date Last Accessed: {:>20} | Date Created: {:>20}".format(item[0],item[1],item[2])
#    print(line)