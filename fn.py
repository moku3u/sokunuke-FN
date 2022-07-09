import keyboard
import pyautogui
from tkinter import *
import time

loop = Tk()

def process():
    keyboard.press("esc")
    time.sleep(0.1)
    pyautogui.click(55, 1015)
    pyautogui.click(260, 1015)
    time.sleep(0.1)
    pyautogui.click(260, 1015)

keyboard.add_hotkey("F1", process)

loop.mainloop()
