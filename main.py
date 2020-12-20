#
#
# THIS FILE IS REQUIRED FOR OPERATION OF THE GPT-4 CLIENT
#
#

import time
import requests
import auth
import startup
import datacollection
from pathlib import Path
import os
import sys
import json
from prompt_toolkit.shortcuts import set_title
from subprocess import call

def clear():
    _ = call('clear' if os.name =='posix' else 'cls') \

clear()

def TERM():
    set_title("GPT-4 Client")

def spacing():
    print(' ')

def loadConfigFiles(files):
    d = []
    path = Path('json')
    if not path.exists():
        path.mkdir(parents=True, exist_ok=True)
    exists = True
    for i in files:
        file = path/i
        if file.exists():
            with open(str(file.resolve()), 'r') as infile:
                d.append(json.loads(infile.read()))
        else:
            exists = False
            break

    if not exists:
        prefFile = open(str((path/"preferences.json").resolve()), 'w')
        userFile = open(str((path/"userdata.json").resolve()), 'w')
        prefFile.write('{"name": "", "APIkey": "", "keyStatus": "", "lastLogin": ""}')
        userFile.write('{}')
        prefFile.close()
        userFile.close()
        d = [{"name": "", "APIkey": "", "keyStatus": "", "lastLogin": ""}, {}]
    return d

TERM()

# Colours
class GPT4colors:
    if os.name != "nt":
        HEADER = '\033[95m'
        OKBLUE = '\033[94m'
        OKCYAN = '\033[96m'
        OKGREEN = '\033[92m'
        WARNING = '\033[93m'
        FAIL = '\033[91m'
        ENDC = '\033[0m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'
    else:
        HEADER = ''
        OKBLUE = ''
        OKCYAN = ''
        OKGREEN = ''
        WARNING = ''
        FAIL = ''
        ENDC = ''
        BOLD = ''
        UNDERLINE = ''


# startup.StartUp()
startup.StartUp()

datacollection.UserData()
datacollection.CollectData()

from halo import Halo
spinner = Halo(text='Validating...', spinner='dots')
time.sleep(1)
print(' ')
print(GPT4colors.FAIL + "Please make sure you have valid credentials (Your API key) on hand. You can get them from your email inbox or at https://gpt-4.co/accounts/manage" + GPT4colors.ENDC)
time.sleep(2)
print(' ')
print(' ')

URL = 'http://api.gpt-4.co/api/tokens/'
obj, obj2 = loadConfigFiles(['preferences.json', 'userdata.json'])
r = requests.get(url=URL + str(obj['APIkey']), params={'id': ''})

if r.status_code != 200:
    auth.AUTH()

else:
    auth.AUTHDONE()

if KeyboardInterrupt:
    sys.exit(0)
