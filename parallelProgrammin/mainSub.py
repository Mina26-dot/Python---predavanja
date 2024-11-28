#sluzi da mozemo da upravljamo nasim operativnim
#sistemom i da mozemo da zatvaramo i otvaramo programe.

import subprocess
import webbrowser
from os import write

from win10toast import ToastNotifier
import time
import random
import threading


#Podsetnik
toaster = ToastNotifier()
# toaster.show_toast("Reminder!", "Take a break", duration=5)


messages = [
    "Take a break",
    "It`s time to chill",
]

# subprocess.Popen(["notepad.exe"])
#
# webbrowser.get("C:/Program Files/Google/Chrome/Application/chrome.exe %s").open("https://google.com") #%s spaja

# subprocess.Popen(["C:/Program Files/Google/Chrome/Application/chrome.exe"])

#===================================================================

#infinite petlja
#ispisi poruku
#napravi pauzu 10 sekundi

# while True:
#     toaster.show_toast("Reminder", "Take a break", duration = 5)
#     time.sleep(10)
#=============================================================================
#  random

# while True:
#     toaster.show_toast("Reminder", random.choice(messages), duration = 2)
#     time.sleep(3)

#print("Poruka")  # ova poruka se nece prikazati zbog beskonacne petlje.
                 # Da bi se to resilo koriste se Thread-ovi. Radi paralelno.
                 # Paralela mozemo imati koliko hocemo
#=============================================================================
#Threading
# def writeHello():
#     while True:
#         print("Hello World")
#         time.sleep(5)
#
# threadHello = threading.Thread(target = writeHello) #otvara drugu granu
# threadHello.start()
#
# print("Prosao petlju")
#============================================================

#Domaci

def showNotification():
    while True:
        toaster.show_toast("Reminder", random.choice(messages), duration=5)
        time.sleep(3)

showNotification_Thread = threading.Thread(target=showNotification)
showNotification_Thread.start()

print("Hello World")