#!/usr/bin/python
# -*- coding: UTF-8 -*-

import ConfigParser
import os
import time
import logging
import logging.handlers

# 根据设置时间判断文件是否过期
def compare_file_time(keepperiod, file):
    time_of_last_mod = os.path.getctime(file)
    hours_between = (time.time() - time_of_last_mod) / (60*60)
    if hours_between > keepperiod:
        return True
    else:
        return False

#遍历文件并排序
def traverseDirByOSWalk(path, includesubdir):
    file_dic = {}
    path = os.path.expanduser(path)
    for (dirname, subdir, subfile) in os.walk(path):
        #logging.info('dirname is %s, subdir is %s, subfile is %s' % (dirname, subdir, subfile))
        #logging.info('[' + dirname + ']')
        for f in subfile:
            #logging.info(os.path.join(dirname, f))
            stats = os.stat(os.path.join(dirname, f))
            file_dic[os.path.join(dirname, f)] = stats.st_ctime
        if includesubdir == False:
            break

    return sorted(file_dic.items(), lambda x, y: cmp(x[1], y[1]), reverse=True)
    #file_list = sorted(file_dic.items(), lambda x, y: cmp(x[1], y[1]), reverse=True)
    #for item in file_list:
    #    line = "Name: {:<20} | Date Created: {:>20}".format(item[0], time.ctime(item[1]))
    #    logging.info(line)

#根据个数设置删除文件
def cleanFilesByNumber(path, includesubdir, filesnumber):
    sortedList = traverseDirByOSWalk(path, includesubdir)
    i = 1
    for item in sortedList:
        if i > filesnumber:
            line = "{0} | {1}".format(item[0],
                                      time.strftime("%Y-%m-%d %X",
                                                    time.localtime(item[1])))
            os.remove(item[0])
            logging.info("cleaned by number: " + line)
        i = i + 1

#根据时间设置删除文件
def cleanFilesByPeriod(path, includesubdir, keepperiod):
    sortedList = traverseDirByOSWalk(path, includesubdir)
    for item in sortedList:
        if compare_file_time(keepperiod, item[0]) == True:
            #line = "{:<20} | {:>20}".format(item[0], time.ctime(item[1]))
            line = "{0} | {1}".format(item[0],
                                      time.strftime("%Y-%m-%d %X",
                                                    time.localtime(item[1])))
            os.remove(item[0])
            logging.info("cleaned by period: " + line)


def cleanjob():
    # 读取安装写入的配置文件入口(平台及各网元配置文件路径)
    #commonfilepath = './filesCleanerConfig.ini'
    commonfilepath = './config/filesCleanerConfig.ini'
    if os.path.exists(commonfilepath) == False:
        logging.error(commonfilepath+ ' is not exists!!')
    else:
        pathConfig = ConfigParser.ConfigParser()
        pathConfig.readfp(open(commonfilepath))
        secs = pathConfig.sections()
        logging.info(secs)
        for sec in secs:
            # 读取各个配置文件中的配置,放入队列等待处理
            subFilePath = pathConfig.get(sec, 'filepath')
            logging.info("SubFilePath:" + subFilePath)
            subConfig = ConfigParser.ConfigParser()
            if os.path.exists(subFilePath) == False:
                logging.warning(subFilePath+ ' is not exists!!')
            else:
                subConfig.readfp(open(subFilePath))
                subsecs = subConfig.sections()
                for subsec in subsecs:
                    logging.info(subsec)
                    if os.path.exists(subsec) == False:
                        logging.warning(subsec+ ' is not exists!!')
                        continue
                    # 初始化默认值
                    includesubdir = False
                    keepperiod = -1
                    filesnumber = -1
                    if subConfig.has_option(subsec, 'includesubdir'):
                        includesubdir = subConfig.getboolean(subsec, 'includesubdir')
                        logging.debug("includesubdir:" + str(includesubdir))
                    if subConfig.has_option(subsec, 'keepperiod'):
                        keepperiod = subConfig.getint(subsec, 'keepperiod')
                        logging.debug("keepperiod(Hours):" + str(keepperiod))
                        cleanFilesByPeriod(subsec, includesubdir, keepperiod)
                    if subConfig.has_option(subsec, 'filesnumber'):
                        filesnumber = subConfig.getint(subsec, 'filesnumber')
                        logging.debug("filesnumber:" + str(filesnumber))
                        cleanFilesByNumber(subsec, includesubdir, filesnumber)

if __name__ == '__main__':
    # log maxsize:10M count:5 日志文件生成脚本存放的目录
    if os.path.exists("./log") == False:
        os.mkdir(os.curdir + os.sep + "log")

    handler = logging.handlers.RotatingFileHandler("./log/filesCleaner.log",
                                                   maxBytes=1073741824,
                                                   backupCount=5)
    datefmt = '%Y-%m-%d %H:%M:%S'
    format_str = '%(asctime)s [%(levelname)s] %(message)s '
    formatter = logging.Formatter(format_str, datefmt)
    handler.setFormatter(formatter)

    clean_logger = logging.getLogger()
    clean_logger.setLevel(logging.DEBUG)
    clean_logger.addHandler(handler)

    logging.info("=============Clean job go!=================")
    cleanjob()
    logging.info("=============Clean job done!=================\n")
