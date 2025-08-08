import time
import pyperclip
import pyautogui as pg
import shutil
import os
import je_open_cv


h = None
while h is None:
    h = pg.locateCenterOnScreen('D:/wps/winamp.png', confidence=0.9)

pg.click((h), clicks=1, interval=1, button='left')

pg.hotkey('Alt', '3')

r = None
while r is None:
    r = pg.locateCenterOnScreen('D:/wps/ID3-window.png', confidence=0.9)

pg.moveTo(r)
pg.moveRel(-264, 58, duration=.1)
pg.dragRel(2500, 0, duration=.6) 

time.sleep(0.1)

pg.hotkey('Ctrl', 'c')
pg.hotkey('Esc')

s = pyperclip.paste()
print(s)

shutil.copy((s), 'D:\Musikk\python copy script')

pg.click((h), clicks=1, interval=1, button='left') 

