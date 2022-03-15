import pyautogui
from time import sleep
from PIL import Image
import cv2
import pytesseract

pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

dictionary = open("7b.dict", 'r')
readdict = dictionary.read()

ilee = 1
sleep(3)

for i in range(ilee):
    skrin = pyautogui.screenshot(region=(690,250, 750,62))
    skrin.save('lingos.png')
    img = cv2.imread('lingos.png')
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    textBef = pytesseract.image_to_string(img, lang='pol')
    print(textBef)
    print(readdict.find(textBef))

    if textBef in readdict:
        pyautogui.typewrite('cheetah')
        pyautogui.press('enter')
        sleep(1.5)
        pyautogui.press('enter')

# https://www.youtube.com/watch?v=6DjFscX4I_c
# Trzeba na komputerze klienta zainstalowac tesseract i polski jezyk rozpoznawania
