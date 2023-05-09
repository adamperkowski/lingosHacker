from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
#from time import sleep

PATH = "C:\\Program Files (x86)\\chromedriver.exe"
driver_service = Service(executable_path=PATH)
driver = webdriver.Chrome(service=driver_service)

driver.get("https://lingos.pl/students/learning")

cred = open('cred.txt', 'r')
credlist = cred.readlines()
find = driver.find_element(By.NAME, 'login')
find.send_keys(credlist[0])
find = driver.find_element(By.NAME, 'password')
find.send_keys(credlist[1])
cred.close()

driver.find_element(By.XPATH, "//img[@src='/public/svg/rocket']").click()

while True:
    pass