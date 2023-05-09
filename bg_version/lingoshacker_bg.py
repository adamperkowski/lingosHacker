from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

PATH = "C:\\Program Files (x86)\\chromedriver.exe"
driver_service = Service(executable_path=PATH)
driver = webdriver.Chrome(service=driver_service)

driver.get("https://lingos.pl/students/learning")

cred = open('cred.txt', 'r')
credlist = cred.readlines()
login = driver.find_element(By.NAME, 'login')
login.send_keys(credlist[0])
login = driver.find_element(By.NAME, 'password')
login.send_keys(credlist[1])
cred.close()

while True:
    pass