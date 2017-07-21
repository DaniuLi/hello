#!/usr/bin/python
# -*- coding: UTF-8 -*-

import fnmatch
import logging
import logging.handlers
import os
import shutil
import time
from tkinter import *
from tkinter import Radiobutton, messagebox
from tkinter.filedialog import askdirectory
from tkinter.scrolledtext import ScrolledText

import exifread


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
    sortedDir = desPath.get() + os.sep + time.strftime('%Y%m%d%H%M%S',
                                                       time.localtime(time.time()))
    index = 1
    for path in all_files(paths, '*.*'):
        f = open(path[2:], 'rb')
        tags = exifread.process_file(f, stop_tag='EXIF DateTimeOriginal')
        time_of_create = ""
        for tag in tags.keys():
            # if tag not in ('JPEGThumbnail', 'TIFFThumbnail', 'Filename', 'EXIF MakerNote'):
            #print ("Key: %s, value %s" % (tag, tags[tag]))
            if tag == 'EXIF DateTimeOriginal':
                if radioVar.get() == 1:
                    time_of_create = str(tags['EXIF DateTimeOriginal'])[
                        0:8].replace(':', '')
                elif radioVar.get() == 2:
                    time_of_create = str(tags['EXIF DateTimeOriginal'])[
                        0:10].replace(':', '')
                break

        if time_of_create == "":
            if radioVar.get() == 1:
                time_of_create = time.strftime(
                    "%Y%m", time.localtime(os.path.getmtime(path)))
            elif radioVar.get() == 2:
                time_of_create = time.strftime(
                    "%Y%m%d", time.localtime(os.path.getmtime(path)))

        dateDir = sortedDir + os.sep + time_of_create
        if os.path.exists(sortedDir) == False:
            os.mkdir(sortedDir)
        if os.path.exists(dateDir) == False:
            os.mkdir(dateDir)

        logging.info("copy %s to %s" % (path, dateDir))
        logText.insert(END, "copy %s to %s \n" % (path, dateDir))
        logText.update()
        shutil.copy2(path, dateDir)

        index += 1

    logText.insert(END, "Total files:%d \n" % (index))


def initLog():
    # log maxsize:10M count:5
    if os.path.exists("./log") == False:
        os.mkdir(os.curdir + os.sep + "log")

    handler = logging.handlers.RotatingFileHandler("./log/sort.log",
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

    logging.info("=============Sort job go!=================")
    logText.delete(1.0, END)
    logText.insert(END, '================go!====================\n')
    sort_files(srcPath.get())
    logging.info("=============Sort job done!=================\n")
    logText.insert(END, '================done!====================\n')
    logText.see(END)
    messagebox.askokcancel('结果提示', '整理完毕')


def selectSrcPath():
    srcPath.set(askdirectory())


def selectDesPath():
    desPath.set(askdirectory())


if __name__ == '__main__':

    root = Tk()

    initLog()

    root.wm_title("文件整理工具")

    srcPath = StringVar()
    desPath = StringVar()
    desPathFormat = "%Y%m"
    desPathLength = 8

    radioVar = IntVar()

    labelSrcPath = Label(root, text="待整理目录:")
    labelSrcPath.grid(row=0, column=0, sticky=W)
    entrySrcPath = Entry(root, textvariable=srcPath, width=60)
    entrySrcPath.grid(row=0, column=1, columnspan=2, sticky=E)
    buttonSrcPath = Button(root, text="目录选择", width=10, command=selectSrcPath)
    buttonSrcPath.grid(row=0, column=3, sticky=E)

    labelDesPath = Label(root, text="输出目录:")
    labelDesPath.grid(row=1, column=0, sticky=W)
    entryDesPath = Entry(root, textvariable=desPath, width=60)
    entryDesPath.grid(row=1, column=1, columnspan=2, sticky=E)
    buttonDesPath = Button(root, text="目录选择",  width=10, command=selectDesPath)
    buttonDesPath.grid(row=1, column=3, sticky=E)

    RadioYM = Radiobutton(
        root, text="按月分类", variable=radioVar, value=1)
    RadioYM.grid(row=2, column=1, sticky=W)
    RadioYM.select()

    RadioYMD = Radiobutton(
        root, text="按天分类", variable=radioVar, value=2)
    RadioYMD.grid(row=2, column=2, sticky=W)

    buttonSort = Button(root, text="开始", width=10, command=sort)
    buttonSort.grid(row=2, column=3,  sticky=E)

    logText = ScrolledText(root)
    logText.grid(row=3, columnspan=4, sticky=W)
    logText.insert(END, '\n\n')
    logText.insert(
        END, '         ================说明====================\n\n\n\n')
    logText.insert(END, '1、把待整理目录下所有文件按时间分类，并拷贝到输出目录下按(月/天)分目录保存\n\n')
    logText.insert(END, '2、如果文件为照片，且带有EXIF信息，则按EXIF中的照片拍摄时间信息进行分类\n')

    root.mainloop()


#pyinstaller -F -w -p C:\Python35-32\Scripts FilesSort.py