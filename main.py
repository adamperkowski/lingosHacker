import pyautogui
from time import sleep
from PIL import Image
import cv2
import pytesseract
from keyboard import is_pressed
from playsound import playsound

pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
inpt = str()

def wyjdz():
    input('\n [*]  Aby wyłączyć bota, naduś dowolny guzioł  ')
    dictionary.close()
    exit()

print(' [ LINGOS HACKER ]')
sleep(0.2)
print(' [ lingos.pl cheat tool ]')
sleep(0.2)
print(' [ Created by Adaśko ]')
sleep(0.2)
print(' [ GitHub: adas1per ]')
sleep(0.2)
print(' [ Discord: adask00#0232 ]')
sleep(0.2)
print(' [ Snapchat: adaskotodebil ]')
sleep(0.2)
print(' [ Instagram: adas_per ]')
sleep(0.5)
print('---------------------------------')

try:
    dictionary = open("lingos.dict", "r+", encoding='utf8')
    linesdict = dictionary.readlines()
except:
    print(' [!]  Wystąpiły problemy z bazą danych. Ponowne przeinstalowanie programu lub pobranie bazy powinno rozwiązać ten problem')
    wyjdz()

sleep(0.5)

ilee = int(input(" [?]  Wprowadź liczbę słów (1 lekcja = 20 słów)   "))

if ilee == 0:
    print(" [*]  Mam nadzieję że wrócisz 😥")
    wyjdz()

print(' [*]  Zmień okno na Firefoxa i naduś F1')

while is_pressed('f1') != True:
    continue
else:
    #--------------------------------------------------------------------------MAIN--------------------------------------------------------------------------
    for i in range(ilee):
        x = int()
        sleep(1.5)
    
        skrin = pyautogui.screenshot(region=(690,262, 750,30))
        skrin.save('lingos.png')
    
        img = cv2.imread('lingos.png')
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    
        textBef = pytesseract.image_to_string(img, lang='pol')
    
        if textBef in linesdict:
        #    if linesdict.count(textBef) > 1:
    
            print(f'\n{textBef}')
            
            pyautogui.typewrite(linesdict[linesdict.index(textBef)+1])
            pyautogui.press('enter')
            sleep(1.5)
            pyautogui.press('enter')
    
        elif textBef == 'Nowe słowo od nauczyciela!\n':
            print('''\n [*]  Nowe słowo!
     [*]  Zostanie dodane do bazy danych automatycznie.''')
    
            #1 ----------------------------------------------------
            skrin = pyautogui.screenshot(region=(703,384, 593,30))
            skrin.save('lingos.png')
    
            img = cv2.imread('lingos.png')
            img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        
            textBef = pytesseract.image_to_string(img, lang='pol')
            print(f'\n{textBef}')
    
            if textBef not in linesdict:
            
                dictionary.write(f'\n{str(textBef)}')
                #2 ----------------------------------------------------
                skrin = pyautogui.screenshot(region=(703,355, 655,30))
                skrin.save('lingos.png')
    
                img = cv2.imread('lingos.png')
                img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    
                textBef = pytesseract.image_to_string(img, lang='pol')
                print(f'\n{textBef}')
    
                dictionary.write(f'{str(textBef)}')
    
                pyautogui.click(pyautogui.locateOnScreen('dalej.png'))
                sleep(0.9)
    
                i = i - 1
                dictionary.close()
                dictionary = open("lingos.dict", "r+", encoding='utf8')
                linesdict = dictionary.readlines()
            else:
                pyautogui.click(pyautogui.locateOnScreen('dalej.png'))
                sleep(0.9)
                i = i - 1
    
        else:
            print(f'\n{textBef}')
            #playsound(u"oof.mp3")
            inpt = input('''\n [!]  Słowo nie zostało znalezione w bazie danych
     [?]  Czy chcesz dodać je do bazy danych?  (T/n)    ''')
    
            if inpt == 'T' or inpt == 't':
                try:
                    inpt = str(input('\n [?]  Wpisz słowo po polsku (musi być DOKŁADNIE tak samo jak w lingosie)    '))
                    dictionary.write(f"\n{inpt}")
                    inpt = str(input('\n [?]  Wpisz słowo po angielsku    '))
                    dictionary.write(f"\n{inpt}\n")
    
                    print('\n [*]  Słowo zostało pomyślnie dodane do bazy danych. Wróć do Firefoxa i naduś F1    ')

                    while is_pressed('f1') != True:
                        continue
    
                    dictionary.close()
                    dictionary = open("lingos.dict", "r+", encoding='utf8')
                    linesdict = dictionary.readlines()
                except:
                    input('\n [!]  Wystąpił problem z dodaniem słowa do bazy danych. Jeśli błąd będzie się powtarzał, skontaktuj się ze mną na FB lub Discordzie    ')
                    wyjdz()
    
            else:
                print('\n [*]  W takim razie musisz wpisać i zatwierdzić je ręcznie :(    ')
                print('\n [*]  Wróć do Firefoxa i naduś F1    ')

                while is_pressed('f1') != True:
                    continue
    
    wyjdz()
    #--------------------------------------------------------------------------END OF MAIN--------------------------------------------------------------------------
