#!/usr/bin/python
# -*- coding: UTF-8 -*-

import fnmatch
import json
import logging
import logging.handlers
import os
import time
import shutil
import exifread
from exifread import __version__, process_file
from exifread.tags import DEFAULT_STOP_TAG, FIELD_TYPES


def all_files(root, patterns='*', single_level=False, yield_folders=False):
    patterns = patterns.split(';')
    for path, subdirs, files in os.walk(root):
        if yield_folders:
            files.extend(subdirs)
        files.sort()
        for name in files:
            for pattern in patterns:
                if fnmatch.fnmatch(name, pattern):
                    yield os.path.join(path, name)
                    break
                if single_level:
                    break

def sort_files(paths):
    index = 1
    for path in all_files(paths, '*.*'):
        f = open(path[2:], 'rb')
        tags = exifread.process_file(f,stop_tag='EXIF DateTimeOriginal')
        time_of_create = ""
        for tag in tags.keys():
            #if tag not in ('JPEGThumbnail', 'TIFFThumbnail', 'Filename', 'EXIF MakerNote'):
            #print ("Key: %s, value %s" % (tag, tags[tag]))
            if tag == 'EXIF DateTimeOriginal':
                time_of_create = str(tags['EXIF DateTimeOriginal'])[0:10].replace(':', '')
                break

        if time_of_create == "":
            time_of_create = time.strftime("%Y%m%d", time.localtime(os.path.getmtime(path)))

        logging.info("copy %s to %s" % (path, time_of_create))


        dateDir = sortedDir + os.sep + time_of_create

        if os.path.exists(dateDir) == False:
            os.mkdir(dateDir)

        shutil.copy(path,dateDir)

        index += 1



if __name__ == '__main__':
    # log maxsize:10M count:5 日志文件生成脚本存放的目录
    if os.path.exists("./log") == False:
        os.mkdir(os.curdir + os.sep + "log")

    handler = logging.handlers.RotatingFileHandler("./log/photoSort.log",
                                                   maxBytes=1073741824,
                                                   backupCount=5)
    datefmt = '%Y-%m-%d %H:%M:%S'
    format_str = '%(asctime)s [%(levelname)s] %(message)s '
    formatter = logging.Formatter(format_str, datefmt)
    handler.setFormatter(formatter)

    clean_logger = logging.getLogger()
    clean_logger.setLevel(logging.INFO)
    clean_logger.addHandler(handler)

    logging.info("=============Sort job go!=================")

    sortedDir = os.curdir + os.sep + "sorted";

    if os.path.exists(sortedDir) == False:
        os.mkdir(sortedDir)

    ##all_files("C:\workspace\photosort")
    sort_files("C:\workspace\photosort")

    logging.info("=============Sort job done!=================\n")
