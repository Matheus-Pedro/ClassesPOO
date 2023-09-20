import tkinter as tk
from tkinter import ttk

janela = tk.Tk()
janela.geometry('400x400')
janela.resizable(True, True)
janela.title('Aluno')  # Título da janela

label_name = tk.Label(text="Nome")
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

label_email = tk.Label(text='E-mail')
label_email.pack()
input_email = tk.Entry()
input_email.pack()

label_adress = tk.Label(text='Endereço')
label_adress.pack()
input_adress = tk.Entry()
input_adress.pack()

label_curse = tk.Label(text='Curso')
label_curse.pack()
input_curse = tk.Entry()
input_curse.pack()

label_class = tk.Label(text='Turma')
label_class.pack()
input_class = tk.Entry()
input_class.pack()

label_period = tk.Label(text='Período')
label_period.pack()
input_period = tk.Entry()
input_period.pack()

exit_button = ttk.Button(janela, text='Fechar', command=lambda: janela.quit())

exit_button.pack(ipadx=5, ipady=10, expand=True)

janela.mainloop()
