#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
import sys
if sys.version_info[0] >= 3:
    import PySimpleGUI as sg
else:
    import PySimpleGUI27 as sg

def Everything():
    sg.ChangeLookAndFeel('TanBlue')

    layout = [
        [sg.Text('待整理目录', size=(15, 1), auto_size_text=False, justification='left'),
         sg.InputText('Default Folder', key='folder', do_not_clear=True), sg.FolderBrowse()],
        [sg.Text('整理后目录', size=(15, 1), auto_size_text=False, justification='left'),
         sg.InputText('Default Folder', key='folder', do_not_clear=True), sg.FolderBrowse()],
        [sg.Text('          '),sg.Radio('按月分类', "RADIO1", key='rad1', default=True),
         sg.Radio('按天分类', "RADIO1", key='rad2')],
        [sg.Multiline(default_text='This is the default Text should you decide not to type anything', size=(65,30),
                      key='multi1', do_not_clear=True)],
        [sg.Submit(), sg.Exit()]
    ]

    window = sg.Window('文件自动整理工具', default_element_size=(40, 1), grab_anywhere=False)
    # button, values = window.LayoutAndRead(layout, non_blocking=True)
    window.Layout(layout)

    while True:
        event, values = window.Read()

        if event is 'SaveSettings':
            filename = sg.PopupGetFile('Save Settings', save_as=True, no_window=True)
            window.SaveToDisk(filename)
            # save(values)
        elif event is 'LoadSettings':
            filename = sg.PopupGetFile('Load Settings', no_window=True)
            window.LoadFromDisk(filename)
            # load(form)
        elif event in ['Exit', None]:
            break

    # window.CloseNonBlocking()


if __name__ == '__main__':
    Everything()