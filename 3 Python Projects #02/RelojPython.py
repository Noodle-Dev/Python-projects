#Noodle Dev
from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title("Reloj en python")
clockFormat = '%H:%M:%S %p'
textFont = "Minecraft"

def time():
    string = strftime(clockFormat)
    label.config(text = string)
    label.after(1000, time)

label = Label(root, font = (textFont, 80), background = "black", foreground = "green")
label.pack(anchor = "center")

time()
mainloop()
