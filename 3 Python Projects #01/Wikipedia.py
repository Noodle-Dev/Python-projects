#Noodle Dev
import wikipedia
import tkinter as tk

global result

def search():
    wikipediaSearch = tk.Tk()
    L = tk.Label(wikipediaSearch, text = entlvar.get())
    L.pack()
    T = tk.Text(wikipediaSearch, height = 10, width = 52)
    T.pack()
    result = wikipedia.summary(entlvar.get(), sentences = 2)
    T.insert(tk.END, result)

wikipediaSearch = tk.Tk()

L = tk.Label(wikipediaSearch, text = 'Busqueda').grid(row = 0)
entlvar = tk.StringVar()
enl = tk.Entry(wikipediaSearch, textvariable = entlvar)
enl.grid(row = 0, column = 1)

tk.Button(wikipediaSearch, text = 'Salir', command = wikipediaSearch.quit).grid(row = 3, column = 0, sticky  = tk.W, pady = 4)
tk.Button(wikipediaSearch, text = 'Buscar', command = search).grid(row = 3, column = 1, sticky= tk.W, pady = 4)

tk.mainloop()
