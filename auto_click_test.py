import webbrowser as wb
import pyautogui as pg
import os 
from os import listdir
import time
from pathlib import Path 
# get the path/directory  
path_of_the_directory= './images'
wb.open('https://aphyuyaung.com')
time.sleep(4)
list_img = ['link1.png','link2.png','link3.png','link4.png']

def autoclick():
    for image in list_img:

    
        link_img = pg.locateCenterOnScreen(image)
        pg.moveTo(link_img)
        pg.click()
        time.sleep(3)
        pg.scroll(-10)
        time.sleep(1)
        pg.scroll(-10)
        time.sleep(2)
        pg.hotkey('alt', 'left')
        time.sleep(3)
        pg.hotkey('alt', 'left')
        time.sleep(3)

images = []

for filename in os.listdir(path_of_the_directory):
    f = os.path.join(path_of_the_directory,filename)
    images.append(f)
for image in images:
    link = None
    print(image)
    while link==None:
        load_more = pg.locateCenterOnScreen('load_more.png')
        that_all = pg.locateCenterOnScreen('That_is_all.png')
        link = pg.locateCenterOnScreen(image)
        if load_more:
            pg.moveTo(load_more)
            pg.click()
            pg.moveTo(100,200)
            time.sleep(3)
        if that_all:
            pg.scroll(100)
            time.sleep(2)
        if link:
            pg.moveTo(link)
            pg.click()
            time.sleep(5)
            pg.scroll(-10)
            time.sleep(3)
            pg.hotkey('alt', 'left')
            time.sleep(3)
            pg.moveTo(100,200)
            break
        else:
            pg.scroll(-5)
            time.sleep(2)

