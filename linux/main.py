import pytesseract
import pyautogui
import cv2

from subprocess import Popen
from time import sleep
from pynput import keyboard

pytesseract.tesseract_cmd = "tesseract"

def wyjdz():
    Popen(['notify-send', "Bot zakończył działanie"])

    input(' [*]  Aby wyłączyć bota, naduś dowolny guzioł  ')
    dictionary.close()

    exit()

def on_release(key):
    if key == keyboard.Key.f1:
        return False

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

try: # lingos.dict
    dictionary = open("lingos.dict", "r+", encoding='utf8')
    linesdict = dictionary.readlines()
except: # Problemy z bazą danych
    print(' [!]  Wystąpiły problemy z bazą danych. Ponowne przeinstalowanie programu lub pobranie bazy powinno rozwiązać ten problem')
    wyjdz()

sleep(0.5)

ilee = int(input(" [?]  Wprowadź liczbę słów (1 lekcja = 20 słów) (wpisz '12345', aby wejść do ustawień)   "))

if ilee == 0:
    print(" [*]  Mam nadzieję że wrócisz 😥")
    wyjdz()
elif ilee == int(12345): # Ustawienia
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

with keyboard.Listener( # F1
        on_release=on_release) as listener:
    listener.join()

#--------------------------------------------------------------------------MAIN--------------------------------------------------------------------------

if notif == 'True':
    Popen(['notify-send', f"No to zaczynamy! Liczba słów: {ilee}"])

for i in range(ilee):
    x = int()
    sleep(1)

    skrin = pyautogui.screenshot(region=(690,262, 750,30))
    skrin.save('lingos.png')

    img = cv2.imread('lingos.png')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    textBef = pytesseract.image_to_string(img, lang='pol')

    if textBef in linesdict: #wpisz i kliknij enter
        print(textBef)

        pyautogui.typewrite(linesdict[linesdict.index(textBef)+1])
        pyautogui.press('enter')
        sleep(1.5)
        pyautogui.press('enter')

    elif textBef == 'Nowen słowo od nauczyciela\n':
        print(''' [*]  Nowe słowo!
 [*]  Zostanie dodane do bazy danych automatycznie.''')

        #1 ----------------------------------------------------
        
        skrin = pyautogui.screenshot(region=(703,384, 593,30))
        skrin.save('lingos.png')

        img = cv2.imread('lingos.png')
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

        textBef = pytesseract.image_to_string(img, lang='pol')
        print(textBef)

        if textBef not in linesdict: # Dodawanie słowa do bazy
            dictionary.write(textBef)

            #2 ----------------------------------------------------

            skrin = pyautogui.screenshot(region=(703,355, 655,30))
            skrin.save('lingos.png')

            img = cv2.imread('lingos.png')
            img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

            textBef = pytesseract.image_to_string(img, lang='pol')
            print(textBef)

            dictionary.write(textBef)

            pyautogui.click(pyautogui.locateOnScreen('dalej.png'))
            sleep(0.9)

            i = - 1
            dictionary.close()
            dictionary = open("lingos.dict", "r+", encoding='utf8')
            linesdict = dictionary.readlines()
        else: # Pomijanie jeśli już jest
            pyautogui.click(pyautogui.locateOnScreen('dalej.png'))
            sleep(0.9)
            i = i - 1
    
    else: # Nie ma w bazie
        if notif == 'True':
            Popen(['notify-send', "Słowo nie zostało znalezione w bazie danych"])

            inpt = input(''' [!]  Słowo nie zostało znalezione w bazie danych
 [?]  Czy chcesz dodać je do bazy danych?  (T/n)    ''')

            if inpt == 'T' or inpt == 't':
                inpt = input(' [?]  Wpisz słowo po polsku(musi być DOKŁADNIE tak samo jak w lingosie)    ')

                if inpt in linesdict:
                    print(f" [!]  Ale '{inpt}' jest już w bazie... Coś się pokićkało...")

                    print(' [*]  Wróć do Firefoxa i naduś F1')
                    with keyboard.Listener( # F1
                        on_release=on_release) as listener:
                            listener.join()
                    
                else:
                    try:
                        dictionary.write(inpt)
                    except:
                        print(' [!]  Wystąpił problem z dodaniem słowa do bazy danych. Jeśli błąd będzie się powtarzał, skontaktuj się ze mną na FB lub Discordzie    ')
                        wyjdz()
                    inpt = str(input(' [?]  Wpisz słowo po angielsku    '))
                    try:
                        dictionary.write(inpt)
                    except:
                        print(' [!]  Wystąpił problem z dodaniem słowa do bazy danych. Jeśli błąd będzie się powtarzał, skontaktuj się ze mną na FB lub Discordzie    ')
                        wyjdz()
                    
                    print(' [*]  Słowo zostało pomyślnie dodane do bazy danych. Wróć do Firefoxa i naduś F1')

                    with keyboard.Listener( # F1
                        on_release=on_release) as listener:
                            listener.join()
                    
                    dictionary.close()
                    dictionary = open("lingos.dict", "r+", encoding='utf8')
                    linesdict = dictionary.readlines()

            else:
                print(' [*]  W takim razie musisz wpisać i zatwierdzić je ręcznie :(    ')
                print(' [*]  Wróć do Firefoxa i naduś F1    ')
                with keyboard.Listener( # F1
                        on_release=on_release) as listener:
                            listener.join()

wyjdz()