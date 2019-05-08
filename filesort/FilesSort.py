#!/usr/bin/python
# -*- coding: UTF-8 -*-
#pyinstaller -F -w -p C:\Python36\Scripts FilesSort.py

import fnmatch
import logging
import logging.handlers
import os
import shutil
import time
import re
import requests
import json
from tkinter import *
from tkinter import Radiobutton, messagebox
from tkinter.filedialog import askdirectory
from tkinter.scrolledtext import ScrolledText
from PIL import Image
import exifread

def latitude_and_longitude_convert_to_decimal_system(*arg):
    """
    经纬度转为小数
    :param arg:
    :return: 十进制小数
    """
    return float(arg[0]) + ((float(arg[1]) + (float(arg[2].split('/')[0]) / float(arg[2].split('/')[-1]) / 60)) / 60)

def find_address_from_GPS(GPS):
    """
    使用Geocoding API把经纬度坐标转换为结构化地址。
    :param GPS:
    :return:
    """
    secret_key = 'WZ1Rt2HMNSG98wKIgFiooFvA6lYteLnI'
    if not GPS['GPS_information']:
        return '该照片无GPS信息'
    lat, lng = GPS['GPS_information']['GPSLatitude'], GPS['GPS_information']['GPSLongitude']
    baidu_map_api = "http://api.map.baidu.com/geocoder/v2/?ak={0}&callback=renderReverse&location={1},{2}s&output=json&pois=0".format(
        secret_key, lat, lng)
    response = requests.get(baidu_map_api)
    content = response.text.replace("renderReverse&&renderReverse(", "")[:-1]
    baidu_map_address = json.loads(content)
    formatted_address = baidu_map_address["result"]["formatted_address"]
    # province = baidu_map_address["result"]["addressComponent"]["province"]
    # city = baidu_map_address["result"]["addressComponent"]["city"]
    # district = baidu_map_address["result"]["addressComponent"]["district"]
    return formatted_address

def find_GPS_image(pic_path):
    GPS = {}
    date = ''
    with open(pic_path, 'rb') as f:
        tags = exifread.process_file(f)
        for tag, value in tags.items():
            if re.match('GPS GPSLatitudeRef', tag):
                GPS['GPSLatitudeRef'] = str(value)
            elif re.match('GPS GPSLongitudeRef', tag):
                GPS['GPSLongitudeRef'] = str(value)
            elif re.match('GPS GPSAltitudeRef', tag):
                GPS['GPSAltitudeRef'] = str(value)
            elif re.match('GPS GPSLatitude', tag):
                try:
                    match_result = re.match('\[(\w*),(\w*),(\w.*)/(\w.*)\]', str(value)).groups()
                    GPS['GPSLatitude'] = int(match_result[0]), int(match_result[1]), int(match_result[2])
                except:
                    deg, min, sec = [x.replace(' ', '') for x in str(value)[1:-1].split(',')]
                    GPS['GPSLatitude'] = latitude_and_longitude_convert_to_decimal_system(deg, min, sec)
            elif re.match('GPS GPSLongitude', tag):
                try:
                    match_result = re.match('\[(\w*),(\w*),(\w.*)/(\w.*)\]', str(value)).groups()
                    GPS['GPSLongitude'] = int(match_result[0]), int(match_result[1]), int(match_result[2])
                except:
                    deg, min, sec = [x.replace(' ', '') for x in str(value)[1:-1].split(',')]
                    GPS['GPSLongitude'] = latitude_and_longitude_convert_to_decimal_system(deg, min, sec)
            elif re.match('GPS GPSAltitude', tag):
                GPS['GPSAltitude'] = str(value)
            elif re.match('.*Date.*', tag):
                date = str(value)
    print("Date:",date)
    return {'GPS_information': GPS, 'date_information': date}

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

def resize_thumbnail(image, size, resample=Image.ANTIALIAS):
    """
    Resize image according to size.
    image:      a Pillow image instance
    size:       a list of two integers [width, height]
    """
    img.thumbnail((size[0], size[1]), resample)
    return img

def file_name(file_dir):   
    L=[]   
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] == '.jpeg':
                L.append(os.path.join(root, file))  
    return L  

def resize_files(paths):
    resizedDir = srcPath.get() + os.sep + time.strftime('%Y%m%d%H%M%S',
                                                       time.localtime(time.time()))
    if os.path.exists(resizedDir) == False:
        os.mkdir(resizedDir)                                                       
    index = 1
    for path in all_files(paths, '*.*'):       
        logText.insert(END, path+'\n')
        try:
            with Image.open(path) as f:
                #image = resize_thumbnail(f,[200,200])
                f.thumbnail((800, 600), Image.ANTIALIAS)
                f.save(resizedDir+os.sep+'resize'+os.path.basename(path), f.format)
                logging.info("resize %s to %s" % (path, resizedDir))      
                logText.insert(END, "resize %s to %s \n" % (path, resizedDir))
                logText.update()
        except BaseException:
            logText.insert(END, "resize %s to %s failed!\n" % (path, resizedDir))
        index += 1

    logText.insert(END, "Total files:%d \n" % (index))

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
        GPS_info = find_GPS_image(path)
        address = find_address_from_GPS(GPS=GPS_info)
        logText.insert(END, "address:%s \n" % (address))
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

def resize():

    logging.info("=============resize job go!=================")
    logText.delete(1.0, END)
    logText.insert(END, '================go!====================\n')
    resize_files(srcPath.get())
    logging.info("=============resize job done!=================\n")
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

    imageWidth = 800
    imageHigth = 600
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

    buttonSort = Button(root, text="开始排序", width=10, command=sort)
    buttonSort.grid(row=2, column=3,  sticky=E)

    labelImageWidth = Label(root, text="宽度:")
    labelImageWidth.grid(row=3, column=1, sticky=W)
    entryImageWidth = Entry(root, textvariable=imageWidth, width=10)
    entryImageWidth.grid(row=3, column=1)

    labelImageHigth = Label(root, text="高度:")
    labelImageHigth.grid(row=3, column=2, sticky=W)
    entryImageHigth = Entry(root, textvariable=imageHigth, width=10)
    entryImageHigth.grid(row=3, column=2)

    buttonResize = Button(root, text="开始调整", width=10, command=resize)
    buttonResize.grid(row=3, column=3,  sticky=E)

    logText = ScrolledText(root)
    logText.grid(row=4, columnspan=4, sticky=W)
    logText.insert(END, '\n\n')
    logText.insert(
        END, '         ================说明====================\n\n\n\n')
    logText.insert(END, '文件日期分类功能：\n\n')
    logText.insert(END, '1、把待整理目录下所有文件按时间分类，并拷贝到输出目录下按(月/天)分目录保存\n\n')
    logText.insert(END, '2、如果文件为照片，且带有EXIF信息，则按EXIF中的照片拍摄时间信息进行分类\n\n')
    logText.insert(END, '   \n\n')
    logText.insert(END, '调整图片尺寸功能：\n\n')
    logText.insert(END, '1、把待整理目录下所有文件按指定宽、高调整，并拷贝到输出目录下保存\n\n')
    root.mainloop()

"""
GPS_info = find_GPS_image(pic_path='123.jpg')
address = find_address_from_GPS(GPS=GPS_info)
print(address)
"""

