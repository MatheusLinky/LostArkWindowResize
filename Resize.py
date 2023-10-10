#By Mattmanxp/Linky

import win32gui
from screeninfo import get_monitors
width = 1280
height = 560
def enumHandler(hwnd, lParam):
    appname = 'LOST ARK'
    if win32gui.IsWindowVisible(hwnd):
        if appname in win32gui.GetWindowText(hwnd):
            win32gui.MoveWindow(hwnd, 0, 0, width, height, True)


for m in get_monitors():
    print(m)
    if m.is_primary==True:
        match m.width:
            case 7680:
                width = m.width
                height = 3340
            case 3840:
                width = m.width
                height = 1670
            case 2560:
                width = m.width
                height = 1135
            case 1920:
                width = m.width
                height = 835
            case 1280:
                width = m.width
                height = 560

win32gui.EnumWindows(enumHandler, None)