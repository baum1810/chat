import requests
from urllib.parse import quote
from os import system
import time

url = "YOUR API LINK"


def senchat(url):
    system("cls")
    username = input("Username\n> ")
    password = input("Password\n> ")
    room = input("Room\n> ")
    message = "a"
    join = 111
    r = requests.get(f"{url}/wchat/{room}/{message}/{username}/{password}/{join}")
    if r.text == "wrong password":
        system("cls")
        print("wrong password")
        system("python client.py")
    elif r.text == "username not registered":
        system("cls")
        print("username not registert")
        time.sleep(3)
        system("python client.py")
    else:
        while True: 
            system("cls")
            join = 0
            message = input(f"Logged in as {username} in room {room}\nmessage\n> ")
            r = requests.get(f"{url}/wchat/{room}/{message}/{username}/{password}/{join}")
            if r.text == "wrong password":
                system("cls")
                print("wrong password")
                system("python client.py")
            elif r.text == "username not registered":
                system("cls")
                print("username not registert")
                time.sleep(3)
                system("python client.py")

def reg(url):
    system("cls")
    username = input("Username\n> ")
    password = input("Password\n> ")
    r = requests.get(f"{url}/register/{username}/{password}")
    if r.text == "Username already registerd":
        system("cls")
        print("Username is already registerd")
        time.sleep(3)
        reg(url)
    else:
        system("cls")
        print("Account Created")
        time.sleep(3)
        senchat(url)

reglog = int(input("[1] login\n[2] register\n> "))

if reglog == 1:
    senchat(url)
elif reglog == 2:
    reg(url)

