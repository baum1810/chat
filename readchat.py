import requests
from urllib.parse import quote
from os import system
doub = 0
url = "YOURAPILINK"
system("cls")
room = input("room\n> ")
system(f"title Room: {room}")
system("cls")
while True:
    r = requests.get(f"{url}/rchat/{room}")
    if r.text == doub:
        pass
    else:
        print(r.text)
    
    doub = r.text
