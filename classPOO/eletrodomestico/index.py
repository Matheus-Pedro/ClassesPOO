import tkinter as tk
from tkinter import ttk

window = tk.Tk()
#nome, utilidade, modelo, marca, preco
window.geometry('300x300')
window.resizable(True, True)
window.title('Eletrodoméstico')

label_name = tk.Label(text='Name')
label_name.pack()
input_name = tk.Entry()
input_name.pack()

label_utility = tk.Label(text='Utilidade')
label_utility.pack()
input_utility = tk.Entry()
input_utility.pack()

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
