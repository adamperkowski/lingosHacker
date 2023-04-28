import pyautogui
from time import sleep
from PIL import Image
import cv2
import pytesseract
from keyboard import is_pressed
from colorama import Fore, init, Style
init()

pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
inpt = str()

def wyjdz():
    if notif == 'True':
            pyautogui.alert(text='Bot zakończył działanie', title='Lingos Hacker', button='OK')

    input(f'\n [*]  Aby wyłączyć bota, naduś dowolny guzioł  ')
    dictionary.close()

    exit()

try:
    Xnotif = open("notifications.option")
except:
    Xnotif = open("notifications.option", 'a')
    Xnotif.close()
    Xnotif = open("notifications.option")

notif = Xnotif.read()
Xnotif.close()

print(f' [ {Fore.RED}L{Fore.GREEN}I{Fore.YELLOW}N{Fore.BLUE}G{Fore.MAGENTA}O{Fore.CYAN}S {Fore.RED}H{Fore.GREEN}A{Fore.YELLOW}C{Fore.BLUE}K{Fore.MAGENTA}E{Fore.CYAN}R {Fore.RESET}]')
sleep(0.2)
print(f' [ {Fore.GREEN}lingos{Fore.RESET}.pl {Fore.RED}cheat{Fore.RESET} tool ]')
sleep(0.2)
print(f' [ Discord: {Fore.BLUE}•••#0232{Fore.RESET} ]')
sleep(0.5)
print('---------------------------------')

try:
    dictionary = open("lingos.dict", "r+", encoding='utf8')
    linesdict = dictionary.readlines()
except:
    print(f' [{Fore.RED}!{Fore.RESET}]  Wystąpiły problemy z bazą danych. Ponowne przeinstalowanie programu lub pobranie bazy powinno rozwiązać ten problem')
    wyjdz()

sleep(0.5)

print(f" [{Fore.BLUE}?{Fore.RESET}]  ", end='')
ilee = int(input("Wprowadź liczbę słów (1 lekcja = 20 słów) (wpisz '12345', aby wejść do ustawień)   "))

if ilee == 0:
    print(f" [{Fore.GREEN}*{Fore.RESET}]  Mam nadzieję że wrócisz 😥")
    wyjdz()
elif ilee == int(12345):
    print('''---------------------------------USTAWIENIA---------------------------------
  [ 1 ]  Powiadomienia
''')

    inpt = int(input('Wybierz opcję:    '))

    if inpt == 1:
        ustaw = open("notifications.option", "w")

        print(f" [{Fore.BLUE}?{Fore.RESET}]  ", end='')
        inpt = input('Włączyć/wyłączyć powiadomienia? (wł/wył)   ')

        if inpt == 'wł' or inpt == 'Wł' or inpt == 'WŁ' or inpt == 'wŁ':
            ustaw.write('True')
        else:
            ustaw.write('False')
        ustaw.close()
            
    else:
        print(f' [{Fore.RED}!{Fore.RESET}]  Niestety nie ma takiej opcji 😞')

    wyjdz()

print(f' [{Fore.GREEN}*{Fore.RESET}]  Zmień okno na Firefoxa i naduś F1\n')

while is_pressed('f1') != True:
    continue

#--------------------------------------------------------------------------MAIN--------------------------------------------------------------------------
#if notif == 'True':
    #powiadomienie

for i in range(ilee):
    x = int()
    sleep(1)

    pyautogui.screenshot(region=(690,262, 750,30)).save('lingos.png')

    img = cv2.imread('lingos.png')
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

    textBef = str(pytesseract.image_to_string(img, lang='pol'))

    if textBef in linesdict:
    #    if linesdict.count(textBef) > 1:

        print(textBef.replace('\n', ''))
        
        pyautogui.typewrite(linesdict[linesdict.index(textBef)+1])
        pyautogui.press('enter')
        sleep(1.5)
        pyautogui.press('enter')

    elif textBef == 'Nowe słowo od nauczyciela!\n':
        print(f''' [{Fore.GREEN}*{Fore.RESET}]  Nowe słowo!
 [{Fore.GREEN}*{Fore.RESET}]  Zostanie dodane do bazy danych automatycznie.''')

        #1 ----------------------------------------------------
        skrin = pyautogui.screenshot(region=(703,384, 593,30))
        skrin.save('lingos.png')

        img = cv2.imread('lingos.png')
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    
        textBef = pytesseract.image_to_string(img, lang='pol')
        print(textBef)

        if textBef not in linesdict:
        
            dictionary.write(str(textBef))
            #2 ----------------------------------------------------
            skrin = pyautogui.screenshot(region=(703,355, 655,30))
            skrin.save('lingos.png')

            img = cv2.imread('lingos.png')
            img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

            textBef = pytesseract.image_to_string(img, lang='pol')
            print(f'\n • {textBef}')

            dictionary.write(str(textBef))

            pyautogui.click(pyautogui.locateOnScreen('dalej.png'))
            #sleep(0.2)
            #pyautogui.click()
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
        print(textBef)

        if notif == 'True':
            pyautogui.alert(text='Słowo nie zostało znalezione w bazie', title='Lingos Hacker', button='OK')

        print(f' [{Fore.RED}!{Fore.RESET}]  Słowo nie zostało znalezione w bazie danych')
        #print(f" [{Fore.BLUE}?{Fore.RESET}]  ", end='')
        #print('Czy chcesz dodać je do bazy danych?  (T/n)    ')

        if inpt == 'T' or inpt == 't':
            
            print(f" [{Fore.BLUE}?{Fore.RESET}]  ", end='')
            inpt = str(input('Wpisz słowo po polsku (musi być DOKŁADNIE tak samo jak w lingosie)    '))

            if f'{inpt}\n' in linesdict:
                print(f"\n [{Fore.RED}!{Fore.RESET}]  Ale '{inpt}' jest już w bazie... Coś się pokićkało...")

                print(f'\n [{Fore.GREEN}*{Fore.RESET}]  Wróć do Firefoxa i naduś F1\n')
                while is_pressed('f1') != True:
                    continue
            else:
                try:
                    dictionary.write(f"\n{inpt}")
                except:
                    print(f'\n [{Fore.RED}!{Fore.RESET}]  Wystąpił problem z dodaniem słowa do bazy danych. Jeśli błąd będzie się powtarzał, skontaktuj się ze mną na FB lub Discordzie    ')
                    wyjdz()
                print(f" [{Fore.BLUE}?{Fore.RESET}]  ", end='')
                inpt = str(input('Wpisz słowo po angielsku    '))
                try:
                    dictionary.write(f"\n{inpt}")
                except:
                    print(f'\n [{Fore.RED}!{Fore.RESET}]  Wystąpił problem z dodaniem słowa do bazy danych. Jeśli błąd będzie się powtarzał, skontaktuj się ze mną na FB lub Discordzie    ')
                    wyjdz()

                print(f'\n [{Fore.GREEN}*{Fore.RESET}]  Słowo zostało pomyślnie dodane do bazy danych. Wróć do Firefoxa i naduś F1\n')
                
                while is_pressed('f1') != True:
                    continue

                dictionary.close()
                dictionary = open("lingos.dict", "r+", encoding='utf8')
                linesdict = dictionary.readlines()

        else:
            print(f' [{Fore.GREEN}*{Fore.RESET}]  W takim razie musisz wpisać i zatwierdzić je ręcznie :(    ')
            print(f'\n [{Fore.GREEN}*{Fore.RESET}]  Wróć do Firefoxa i naduś F1    \n')
            while is_pressed('f1') != True:
                continue

wyjdz()
#--------------------------------------------------------------------------END OF MAIN--------------------------------------------------------------------------
