from tkinter import *
import pyautogui
from time import sleep
from PIL import Image
import cv2
import pytesseract

pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

tk = Tk()
tk.title("Lingos Hacker")

#dawaj = Label(tk, text="ILEE??!!! lingos'ów")
#ilee = Entry(tk)
#notka = Label(tk, text='Lingos Hacker by Adam Perkowski (APMP Studios).\nAll Rights Reserved.')
#ileeBut = 
#dawaj.pack()
#ilee.pack()
#notka.pack()

ilee = 1
sleep(3)

for i in range(ilee):
    skrin = pyautogui.screenshot(region=(725,386, 532, 31))
    skrin.save('lingos.png')
    img = cv2.imread('lingos.png')
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    textBef = pytesseract.image_to_string(img)

    pyautogui.typewrite(textBef)
    pyautogui.press('enter')
    sleep(1.5)
    pyautogui.press('enter')


# https://www.youtube.com/watch?v=6DjFscX4I_c
# Trzeba na komputerze klienta zainstalowac tesseract i polski jezyk rozpoznawania
