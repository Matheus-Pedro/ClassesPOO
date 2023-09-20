import tkinter as tk
from tkinter import ttk

window = tk.Tk()

window.geometry('300x400')
window.resizable(True, True)
window.title('Smartphone')

label_color = tk.Label(text='Cor')
label_color.pack()
input_color = tk.Entry()
input_color.pack()

label_year = tk.Label(text='Ano de lançamento')
label_year.pack()
input_year = tk.Entry()
input_year.pack()

label_model = tk.Label(text='Modelo')
label_model.pack()
input_model = tk.Entry()
input_model.pack()

label_brand = tk.Label(text='Marca')
label_brand.pack()
input_brand = tk.Entry()
input_brand.pack()

label_price = tk.Label(text='Preço')
label_price.pack()
input_price = tk.Entry()
input_price.pack()

window.mainloop()
