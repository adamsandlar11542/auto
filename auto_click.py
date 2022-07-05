#importing modules
import webbrowser as wb
import pyautogui as pg
import os 
from os import listdir
import time

from sympy import imageset


list_img = ['link1.png','link2.png','link3.png','link4.png']
# # folder_dir = "./images" 
# # for images in os.listdir(folder_dir):
# #     print(images)
# #     type(images)
# # check if the image ends with png)
def autoclick():
    #open the webbrowser with the link
    wb.open('https://aphyuyaung.com')
    time.sleep(3)
    #search for the link
    read_more = pg.locateCenterOnScreen('read_more.png')
    # move = pg.center(res)
    pg.moveTo(read_more)
    pg.click()
    time.sleep(3)
    for image in list_img:

    
        link_img = pg.locateCenterOnScreen(image)
        pg.moveTo(link_img)
        pg.click()
        time.sleep(3)
        for i in range(10):
            pg.scroll(-100)
            time.sleep(1)
            pg.scroll(100)
        time.sleep(5)
        pg.hotkey('alt', 'left')
        time.sleep(3)
autoclick()
# # pg.scroll()
# def click():
#     pass
# def search():
#     pass
# def delete():
#     pass
# def drag():
#     pass
