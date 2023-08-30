# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os.path
import ctypes
from datetime import datetime


def change_background():
    dt = datetime.now()
    weekday = dt.weekday()

    match weekday:
        case 0:
            ctypes.windll.user32.SystemParametersInfoW(20, 0, os.path.abspath("images/mondayImage.png"), 0)
        case 1:
            ctypes.windll.user32.SystemParametersInfoW(20, 0, os.path.abspath("images/tuesdayImage.png"), 0)
        case 2:
            ctypes.windll.user32.SystemParametersInfoW(20, 0, os.path.abspath("images/wednesdayImage.png"), 0)
        case 3:
            ctypes.windll.user32.SystemParametersInfoW(20, 0, os.path.abspath("images/thursdayImage.png"), 0)
        case 4:
            ctypes.windll.user32.SystemParametersInfoW(20, 0, os.path.abspath("images/fridayImage.png"), 0)
        case 5:
            ctypes.windll.user32.SystemParametersInfoW(20, 0, os.path.abspath("images/saturdayImage.png"), 0)
        case 6:
            ctypes.windll.user32.SystemParametersInfoW(20, 0, os.path.abspath("images/sundayImage.png"), 0)


if __name__ == '__main__':
    change_background()
