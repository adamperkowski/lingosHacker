from tkinter import *
import pyautogui
from time import sleep
from PIL import Image
import cv2
import pytesserac

pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

tk = Tk()
tk.title("Lingos Hacker")

dawaj = Label(tk, text="ILEE??!!! lingos'ów")
ilee = Entry(tk)
notka = Label(tk, text='Lingos Hacker by Adam Perkowski (APMP Studios).\nAll Rights Reserved.')
dawaj.pack()
ilee.pack()
notka.pack()

for i in range(ilee)
    skrin = pyautogui.screenshot(region=(725,386, 532, 31))
    skrin.save('lingos - nie usuwac.png')
    img = cv2.imread('lingos - nie usuwac.png')
    img = cv2.cvtColor(img,cv2.COLOR_BRG2RGB)
    textBef = pytesseract.image_to_string(img)

    pyautogui.typewrite(textBef)
    pyautogui.press('enter')
    sleep(1.5)
    pyautogui.press('enter')


# https://www.youtube.com/watch?v=6DjFscX4I_c
# Trzeba na komputerze klienta zainstalowac tesseract i polski jezyk rozpoznawania
