import pyautogui
from time import sleep
from PIL import Image
import cv2
import pytesseract
from keyboard import is_pressed
from playsound import playsound
from notifypy import Notify

pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
inpt = str()

def wyjdz():
    notification = Notify()
    notification.title = "Lingos Hacker"
    notification.message = "Bot zakończył działanie"
    notification.icon = "lingoshecker.png"
    notification.application_name = "Lingos Hacker"
    notification.send()

    input('\n [*]  Aby wyłączyć bota, naduś dowolny guzioł  ')
    dictionary.close()

    exit()

Xnotif = open("notifications.option")
notif = Xnotif.read()
Xnotif.close()

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

ilee = int(input(" [?]  Wprowadź liczbę słów (1 lekcja = 20 słów) (wpisz '12345', aby wejść do ustawień)   "))

if ilee == 0:
    print(" [*]  Mam nadzieję że wrócisz 😥")
    wyjdz()
elif ilee == int(12345):
    print('''---------------------------------USTAWIENIA---------------------------------
  [ 1 ]  Powiadomienia
''')

    inpt = int(input('Wybierz opcję:    '))

    if inpt == 1:
        ustaw = open("notifications.option", "w")

        inpt = input('  [?]  Włączyć/wyłączyć powiadomienia? (wł/wył)   ')

        if inpt == 'wł' or inpt == 'Wł' or inpt == 'WŁ' or inpt == 'wŁ':
            ustaw.write('True')
        else:
            ustaw.write('False')
        ustaw.close()
            
    else:
        print(' [!]  Niestety nie ma takiej opcji :(')

    wyjdz()

print(' [*]  Zmień okno na Firefoxa i naduś F1')

while is_pressed('f1') != True:
    continue

#--------------------------------------------------------------------------MAIN--------------------------------------------------------------------------
if notif == 'True':
    notification = Notify()
    notification.title = "No to zaczynamy!"
    notification.message = f"Liczba słów: {ilee}"
    notification.icon = "lingoshecker.png"
    notification.application_name = "Lingos Hacker"
    notification.send()

for i in range(ilee):
    x = int()
    sleep(1)

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

        notification = Notify()
        notification.title = "Nieznane słowo"
        notification.message = "Słowo nie zostało znalezione w bazie danych"
        notification.icon = "lingoshecker.png"
        notification.application_name = "Lingos Hacker"
        notification.send()

        inpt = input(''' [!]  Słowo nie zostało znalezione w bazie danych
 [?]  Czy chcesz dodać je do bazy danych?  (T/n)    ''')

        if inpt == 'T' or inpt == 't':

            inpt = str(input('\n [?]  Wpisz słowo po polsku (musi być DOKŁADNIE tak samo jak w lingosie)    '))

            if f'{inpt}\n' in linesdict:
                print(f"\n [!]  Ale '{inpt}' jest już w bazie... Coś się pokićkało...")

                print('\n [*]  Wróć do Firefoxa i naduś F1\n')
                while is_pressed('f1') != True:
                    continue
            else:
                try:
                    dictionary.write(f"\n{inpt}")
                except:
                    print('\n [!]  Wystąpił problem z dodaniem słowa do bazy danych. Jeśli błąd będzie się powtarzał, skontaktuj się ze mną na FB lub Discordzie    ')
                    wyjdz()
                inpt = str(input('\n [?]  Wpisz słowo po angielsku    '))
                try:
                    dictionary.write(f"\n{inpt}")
                except:
                    print('\n [!]  Wystąpił problem z dodaniem słowa do bazy danych. Jeśli błąd będzie się powtarzał, skontaktuj się ze mną na FB lub Discordzie    ')
                    wyjdz()

                print('\n [*]  Słowo zostało pomyślnie dodane do bazy danych. Wróć do Firefoxa i naduś F1\n')
                
                while is_pressed('f1') != True:
                    continue

                dictionary.close()
                dictionary = open("lingos.dict", "r+", encoding='utf8')
                linesdict = dictionary.readlines()

        else:
            print('\n [*]  W takim razie musisz wpisać i zatwierdzić je ręcznie :(    ')
            print('\n [*]  Wróć do Firefoxa i naduś F1    ')
            while is_pressed('f1') != True:
                continue

wyjdz()
#--------------------------------------------------------------------------END OF MAIN--------------------------------------------------------------------------
