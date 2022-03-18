import pyautogui
from time import sleep
from PIL import Image
import cv2
import pytesseract

pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

def wyjdz():
    input('\n [*]  Aby wyłączyć bota, naduś dowolny guzioł  ')
    exit()

print(' [ LINGOS HACKER ]')
sleep(0.2)
print(' [ lingos.pl cheat tool ]')
sleep(0.2)
print(' [ Created by Adaśko ]')
sleep(0.2)
print(' [ Discord: 𝕙𝕒𝕜𝕚𝕖𝕣 𝕜𝕝𝕒𝕜𝕚𝕖𝕣#0232 ]')
sleep(0.2)
print(' [ Snapchat: adaskotodebil ]')
sleep(0.2)
print(' [ Instagram: adas_per ]')
sleep(0.5)
print('---------------------------------')

try:
    dictionary = open("lingos.dict", encoding='utf8')
    linesdict = dictionary.readlines()
except:
    print(' [!]  Wystąpiły problemy z bazą danych. Ponowne przeinstalowanie programu lub pobranie bazy powinno rozwiązać ten problem')
    wyjdz()

sleep(0.5)

ilee = int(input(" [?]  Wprowadź liczbę słów (1 lekcja = 20 słów)   "))

if ilee == 0:
    print(" [*]  Mam nadzieję że wrócisz 😥")
    wyjdz()

print(' [*]  Zmień okno na przeglądarkę w ciągu 4.5 sekuny')
sleep(3)

for i in range(ilee):
    x = int()
    sleep(1.5)
    skrin = pyautogui.screenshot(region=(690,250, 750,62))
    skrin.save('lingos.png')
    img = cv2.imread('lingos.png')
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    textBef = pytesseract.image_to_string(img, lang='pol')
    print(textBef)
    if textBef in linesdict:
        for line in linesdict:
            if str(line) == str(textBef):
                pyautogui.typewrite(linesdict[x+1])
                pyautogui.press('enter')
                sleep(1.5)
                pyautogui.press('enter')
                break
            #else:
            #    print('nie ma')
            x = x + 1
    elif textBef == 'Nowe słowo od nauczyciela!\n':
        input('''\n [*]  Nowe słowo!
 [*]  Wpisz je i zatwierdź ręcznie (auto dodawanie do bazy wkrótce)    ''')
    else:
        input(''' [!]  Słowo nie zostało znalezione w bazie danych
 [!]  Musisz wpisać i zatwierdzić je ręcznie    ''')

wyjdz()
