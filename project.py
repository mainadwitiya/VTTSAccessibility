"""Get the current mouse position."""

import logging
import sys
import time
import pyautogui
from win32 import GetSystemMetrics

logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s',
                    level=logging.DEBUG,
                    stream=sys.stdout)


def get_mouse_position():
    """
    Get the current position of the mouse.

    Returns
    -------
    dict :
        With keys 'x' and 'y'
    """
    mouse_position = None
    import sys
    if sys.platform in ['linux', 'linux2']:
        pass
    elif sys.platform == 'win32':
        try:
            import win32api
        except ImportError:
            logging.info("win32api not installed")
            win32api = None
        if win32api is not None:
            x, y = win32api.GetCursorPos()
            mouse_position = {'x': x, 'y': y}
    elif sys.platform == 'Mac':
        pass
    else:
        try:
            import Tkinter  # Tkinter could be supported by all systems
        except ImportError:
            logging.info("Tkinter not installed")
            Tkinter = None
        if Tkinter is not None:
            p = Tkinter.Tk()
            x, y = p.winfo_pointerxy()
            mouse_position = {'x': x, 'y': y}
        print("sys.platform={platform} is unknown. Please report."
              .format(platform=sys.platform))
        print(sys.version)
    return mouse_position


def get_screen_area():
    mouse_coordinates = get_mouse_position()

    screenWidth = GetSystemMetrics(0)
    screenHeight = GetSystemMetrics(1)

    screenshotLocationX = mouse_coordinates['x'] - 250
    screenshotLocationY = mouse_coordinates['y'] - 250

    # if (screenshotLocationX < 250) and (screenshotLocationY < 250):
    #     screenshotLocationX=0
    #     screenshotLocationY=0
    # elif (screenshotLocationX<250) and (screenshotLocationY + 500> screenHeight):
    #     screenshotLocationX=0
    #     screenshotLocationY = screenHeight - 500
    # elif (screenshotLocationX + 500 > screenWidth and screenshotLocationY + 500):
    #     screenshotLocationX = screenWidth - 500
    #     screenshotLocationY = screenHeight - 500
    # elif (screenshotLocationX + 500 > screenWidth and screenshotLocationY<250):
    #     screenshotLocationX = screenWidth - 500
    #     screenshotLocationY = 0

    if screenshotLocationX < 500:
        screenshotLocationX = 0
    if screenshotLocationY < 500:
        screenshotLocationY = 0
    if screenshotLocationX + 500 > screenWidth:
        screenshotLocationX = screenWidth - 500
    if screenshotLocationY + 500 > screenHeight:
        screenshotLocationY = screenWidth - 500

    im = pyautogui.screenshot("screen_region.jpg", region=(
        screenshotLocationX, screenshotLocationY, 500, 500))
    im.show()


get_screen_area()
