import tkinter as tk
from tkinter import ttk

window = tk.Tk()

window.geometry('300x400')
window.resizable(True, True)
window.title('Funcionario')

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

label_address = tk.Label(text='Endereço')
label_address.pack()
input_address = tk.Entry()
input_address.pack()

label_salary = tk.Label(text='Salário')
label_salary.pack()
input_salary = tk.Entry()
input_salary.pack()

label_profession = tk.Label(text='Profissão')
label_profession.pack()
input_profession = tk.Entry()
input_profession.pack()

label_contractduration = tk.Label(text='Duração de contrato')
label_contractduration.pack()
input_contractduration = tk.Entry()
input_contractduration.pack()

label_sector = tk.Label(text='Setor')
label_sector.pack()
input_sector = tk.Entry()
input_sector.pack()

window.mainloop()
