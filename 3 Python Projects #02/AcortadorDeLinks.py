#Noodle Dev
import pyshorteners
from colorama import Fore, init

init()

#INPUT
url = input("Introduzca una URL: ")

#OUTPUT
s = pyshorteners.Shortener().tinyurl.short(url)
print(Fore.GREEN + "Tu URL acortada es: ", s)
