from colorama import Fore, init, Style
print('Lingos Hacker background support BETA.\nUWAGA! Dziala tylko na jedna lekcje.')

from time import sleep
sleep(1)

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from random import choice

try:
    dictionary = open("lingos.dict", "r+", encoding='utf8')
    linesdict = dictionary.readlines()
except:
    print(f'{Fore.RED} [!] Wystapil problem z baza danych. Skontaktuj sie z administratorem :){Fore.RESET}')
    while True:
        pass

options = Options()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

PATH = "C:\\Program Files (x86)\\chromedriver.exe"
driver_service = Service(executable_path=PATH, keep_alive=True)
driver = webdriver.Chrome(service=driver_service, service_log_path='NUL', options=options)
driver.set_page_load_timeout(6)
actions = ActionChains(driver)

print(f'{Fore.CYAN} [*] Loaded successfully.{Fore.RESET}')                                      #Load
#ilee = int(input(f'{Fore.GREEN} [?] Podaj liczbe slow: {Fore.RESET}'))
ilee = 20000

driver.get("https://lingos.pl/students/learning")

cred = open('cred.txt', 'r')
credlist = cred.readlines()
find = driver.find_element(By.NAME, 'login')
find.send_keys(credlist[0])
find = driver.find_element(By.NAME, 'password')
find.send_keys(credlist[1])
cred.close()

driver.implicitly_wait(8)
driver.find_element(By.XPATH, "//img[@src='/public/svg/rocket']").click()
driver.implicitly_wait(8)

for i in range(ilee):
    driver.implicitly_wait(1.5)

    try:
        if driver.find_element(By.CSS_SELECTOR, 'h4.m-0').size != 0:
            textBef = driver.find_element(By.CSS_SELECTOR, 'h3.mb-4').text
            dictionary.write(f"{driver.find_element(By.CSS_SELECTOR, 'h3.mb-0').text}\n")
            dictionary.write(f"{textBef}\n")

            dictionary.close()
            dictionary = open("lingos.dict", "r+", encoding='utf8')
            linesdict = dictionary.readlines()
            driver.find_element(By.CSS_SELECTOR, 'button.w-100').click()
    
    except:
        try:
            textBef = str(driver.find_element(By.ID, 'content_flashcard_section').find_element(By.TAG_NAME, 'h3').text + '\n')
            #textBef = str(driver.find_element(By.CSS_SELECTOR, 'h3.mb-0').text + '\n')
            if linesdict.count(textBef) == 1:
                find = driver.find_element(By.ID, 'answer')
                find.send_keys(linesdict[linesdict.index(textBef)+1])

                actions.send_keys(Keys.RETURN).perform()
                driver.implicitly_wait(8)
            else:
                indexes = [i for i, x in enumerate(linesdict) if x == textBef]
                print(indexes)
                random_index = choice(indexes)

                find = driver.find_element(By.ID, 'answer')
                find.send_keys(linesdict[random_index+1])

                actions.send_keys(Keys.RETURN).perform()
                driver.implicitly_wait(8)
        except:
                input('brak slowa w bazie\n')

print(f'{Fore.CYAN} [*] Bot zakonczyl dzialanie{Fore.RESET}\nWcisnij dowolny przycisk.')
input()
