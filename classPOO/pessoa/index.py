import tkinter as tk
from tkinter import ttk

janela = tk.Tk()

janela.geometry('300x300')
janela.resizable(True, True)
janela.title('Pessoa')

label_name = tk.Label(text='Nome')
label_name.pack()
input_name = tk.Entry()
input_name.pack()

label_cpf = tk.Label(text='CPF')
label_cpf.pack()
input_cpf = tk.Entry()
input_cpf.pack()

label_age = tk.Label(text='Idade')
label_age.pack()
input_age = tk.Entry()
input_age.pack()

label_email = tk.Label(text='Email')
label_email.pack()
input_email = tk.Entry()
input_email.pack()

label_address = tk.Label(text='Endereço')
label_address.pack()
input_address = tk.Entry()
input_address.pack()

janela.mainloop()
