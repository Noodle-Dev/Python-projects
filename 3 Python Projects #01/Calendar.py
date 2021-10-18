#Noodle Dev
from tkinter import *
import calendar

root = Tk()
root.title("Calendario 2021 en python")

year = 2021
myCal = calendar.calendar(year)
cal_year = Label(root, text = myCal, font = "Consolas 10 bold")
cal_year.pack()
root.mainloop()
