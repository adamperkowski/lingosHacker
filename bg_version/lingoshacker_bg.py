from colorama import Fore, init, Style
print('Lingos Hacker background support BETA.')

from time import sleep
sleep(1)

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

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

print(f'{Fore.CYAN} [*] Loaded successfully.{Fore.RESET}')                                      #Load
ilee = int(input(f'{Fore.GREEN} [?] Podaj liczbe lekcji: {Fore.RESET}'))

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