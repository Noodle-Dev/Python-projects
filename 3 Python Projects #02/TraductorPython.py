from tkinter import *
from translate import Translator

root = Tk()
root.title("Traductor")

mainframe = Frame(root)
mainframe.grid(column=0,row=0, sticky=(N,W,E,S) )
mainframe.columnconfigure(0, weight = 1)
mainframe.rowconfigure(0, weight = 1)
mainframe.pack(pady = 10, padx = 10)

lan1 = StringVar(root)
lan2 = StringVar(root)
choices = { 'English','French','Portuguese','Spanish','German'}

lan1.set('Spanish')
lan2.set('English')

def translate():
    translator= Translator(from_lang=lan1.get(),to_lang=lan2.get())
    translation = translator.translate(var.get())
    var1.set(translation)

lan1menu = OptionMenu( mainframe, lan1, *choices)
Label(mainframe,text="Select a language", bg = '#D1BDF3').grid(row = 0, column = 1)
lan1menu.grid(row = 1, column =1)

lan2menu = OptionMenu( mainframe, lan2, *choices)
Label(mainframe,text="Select a language", bg = '#D1BDF3').grid(row = 0, column = 2)
lan2menu.grid(row = 1, column =2)

Label(mainframe, text = "Enter text", bg = '#BAF9F7').grid(row=2,column=0)
var = StringVar()
textbox = Entry(mainframe, textvariable=var).grid(row=2,column=1)

Label(mainframe, text = "Traduction", bg = '#BDF3F1').grid(row=2,column=2)
var1 = StringVar()
textbox = Entry(mainframe, textvariable=var1, ).grid(row=2,column=3)

b=Button(mainframe,text='Translate',command=translate, bg='#A877BA').grid(row=3,column=1,columnspan=3)

root.mainloop()
