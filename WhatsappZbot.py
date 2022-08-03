import pyautogui as pg
import time

time.sleep(10)

txt = open("animal.txt", "r")
a = "qwertyuiopasdfghjklzxcvbnm"

for i in txt:
    pg.write(a + " " + i)
    pg.press("enter")
