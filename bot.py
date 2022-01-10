from pyautogui import *
import time
import pyautogui
# win32api is faster that pyautogui
import win32api
import win32con
import keyboard


def click(x, y):
    win32api.SetCursorPos((x, y))
    # press down
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.1)
    # release
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


click(386, 523)


# pyautogui.displayMousePosition()
while keyboard.is_pressed('q') == False:
    im = pyautogui.screenshot()
    px1 = im.getpixel((340, 420))
    px2 = im.getpixel((227, 420))
    px3 = im.getpixel((445, 400))
    px4 = im.getpixel((550, 400))
    if px1[0] == 0:
        click(340, 420)
    if px2[0] == 0:
        click(227, 420)
    if px3[0] == 0:
        click(445, 400)
    if px4[0] == 0:
        click(550, 400)


# clever way to have mouse you want
