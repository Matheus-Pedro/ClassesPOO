import tkinter as tk
from tkinter import ttk

janela = tk.Tk()

janela.geometry('300x300')
janela.resizable(True, True)
janela.title('Conta a pagar')

label_name = tk.Label(text='Nome')
label_name.pack()
input_name = tk.Entry()
input_name.pack()

label_description = tk.Label(text='Descrição')
label_description.pack()
input_description = tk.Entry()
input_description.pack()

label_value = tk.Label(text='Valor')
label_value.pack()
input_value = tk.Entry()
input_value.pack()

label_duedate = tk.Label(text='Valor')
label_duedate.pack()
input_duedate = tk.Entry()
input_duedate.pack()

janela.mainloop()
