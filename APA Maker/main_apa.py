import tkinter as tk

def create_citation():
    title = entry_title.get()
    author = entry_author.get()
    url = entry_url.get()
    access_date = entry_access_date.get()

    citation = f"{author}. ({access_date}). {title}. Extraido de {url}"
    citation_label.config(text=citation)
    citation_text = citation_label.cget("text")
    window.clipboard_clear()
    window.clipboard_append(citation_text)

# Main window configuration
window = tk.Tk()
window.title("Creador de citas")
window.geometry("600x400")

tk.Label(window, text="Titulo del articulo:").pack(pady=5)
entry_title = tk.Entry(window, width=50)
entry_title.pack(pady=5)

tk.Label(window, text="Autor:").pack(pady=5)
entry_author = tk.Entry(window, width=50)
entry_author.pack(pady=5)

tk.Label(window, text="URL del Articulo:").pack(pady=5)
entry_url = tk.Entry(window, width=50)
entry_url.pack(pady=5)

tk.Label(window, text="Fecha de extracion (YYYY-MM-DD):").pack(pady=5)
entry_access_date = tk.Entry(window, width=50)
entry_access_date.pack(pady=5)

create_citation_button = tk.Button(window, text="Crear cita", command=create_citation)
create_citation_button.pack(pady=10)

citation_label = tk.Label(window, text="", wraplength=550, justify="center", font=("Arial", 12))
citation_label.pack(pady=20)

window.mainloop()
