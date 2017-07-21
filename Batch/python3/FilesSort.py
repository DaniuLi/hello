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
from tkinter import *
from tkinter.filedialog import askdirectory
from tkinter import messagebox
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText


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
    #sortedDir = os.curdir + os.sep + "sorted" + time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()));
    sortedDir = desPath.get() + os.sep + time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()));
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
        logText.insert(END, "copy %s to %s \n" % (path, time_of_create))

        dateDir = sortedDir + os.sep + time_of_create
        if os.path.exists(sortedDir) == False:
            os.mkdir(sortedDir)
        if os.path.exists(dateDir) == False:
            os.mkdir(dateDir)

        shutil.copy2(path,dateDir)

        index += 1


def initLog():
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

def sort():
    # 非定量进度条
    #flag = False  # 标志位
    #value = 0  # 进度条位置

    #p2 = ttk.Progressbar(root, length=200, mode="indeterminate", orient=HORIZONTAL)
    #p2.grid(row=2, column=1)

    #p2.start(10)
    logging.info("=============Sort job go!=================")
    logText.delete(1.0,END)
    logText.insert(END, '================Sort job go!====================\n')
    ##all_files("C:\workspace\photosort")
    sort_files(srcPath.get())
    logging.info("=============Sort job done!=================\n")
    logText.insert(END, '================Sort job done!====================\n')
    #p2.stop()
    #p2.grid_remove()
    logText.see(END)
    messagebox.askokcancel('结果提示','整理完毕')

def selectSrcPath():
    srcPath.set(askdirectory())

def selectDesPath():
    desPath.set(askdirectory())


root = Tk()

initLog()

root.wm_title("文件整理工具")

srcPath = StringVar()
desPath = StringVar()


labelSrcPath = Label(root, text = "整理目录:")
labelSrcPath.grid(row = 0, column = 0, sticky = W)
entrySrcPath = Entry(root,textvariable=srcPath, width=50)
entrySrcPath.grid(row = 0, column = 1, sticky = E)
buttonSrcPath = Button(root, text ="目录选择", width = 10, command = selectSrcPath)
buttonSrcPath.grid(row = 0, column = 2, sticky = E)

labelDesPath = Label(root, text = "输出目录:")
labelDesPath.grid(row = 1, column = 0, sticky = W)
entryDesPath = Entry(root,textvariable=desPath, width=50)
entryDesPath.grid(row = 1, column = 1, sticky = E)
buttonDesPath = Button(root, text ="目录选择",  width = 10, command = selectDesPath)
buttonDesPath.grid(row = 1, column = 2, sticky = E)

buttonSort = Button(root, text ="开始", width = 10, command = sort)
buttonSort.grid(row = 2, column = 2,  sticky = E)

#s = Scrollbar(root)
logText = ScrolledText(root)
logText.grid(row = 3, columnspan = 3, sticky = W)
#logText.focus_set()
#s.config(command=logText.yview)
#logText.config(yscrollcommand=s.set)


root.mainloop()


