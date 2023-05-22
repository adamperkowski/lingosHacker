import pytesseract
from time import sleep
import cv2
import pyautogui

pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

def ss():
    pyautogui.screenshot(region=(419,966, 70,20)).save('ryby.png')

    img = cv2.imread('ryby.png')
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

    #print(pytesseract.image_to_string(img))
    return pytesseract.image_to_string(img)

sleep(5)

while ss() == 'Fish Again\n':
    pyautogui.click(419,966)

    sleep(4)