from time import sleep
import pyperclip
import re
import os.path
import requests
import msvcrt


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


regex = re.compile(
    r'^(?:http|ftp)s?://'  # http:// or https://
    # domain...
    r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'
    r'localhost|'  # localhost...
    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
    r'(?::\d+)?'  # optional port
    r'(?:/?|[/?]\S+)$', re.IGNORECASE)

clipboard = pyperclip.paste()
isURL = re.match(regex, clipboard) is not None

if not isURL:
    raise TypeError("Not a URL")

print('pc or mobile? (type 0 for pc, 1 for mobile)')
input_char = msvcrt.getwch()
dir = ""
print(input_char)
if input_char == "0":
    dir = f"for pcs"
elif input_char == "1":
    dir = f"for phones"
else:
    raise TypeError("Not a valid directory")

cls()
print(f'selected {dir}, downloading...')

if "preview.redd.it" in clipboard:
    path = os.path.split(clipboard)[1]
    clipboard = f"https://i.redd.it/{path}"

dirList = os.listdir(dir)
dirList = [int(i.split('.')[0]) for i in dirList]
extension = "jpg"
if ".png" in path:
    extension = "png"
elif ".jpg" in path:
    extension = "jpg"

fileName = str(sorted(dirList, reverse=True)[0]+1).zfill(4) + "." + extension

response = requests.get(clipboard)
open(os.path.join(dir, fileName), "wb").write(response.content)
print('download successful')
sleep(0.75)
exit()
