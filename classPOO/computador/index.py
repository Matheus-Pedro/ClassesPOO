import tkinter as tk
from tkinter import ttk

janela = tk.Tk()

janela.geometry('400x400')
janela.resizable(True, True)
janela.title('Computador')

label_ghz = tk.Label(text= 'Ghz do Processador')
label_ghz.pack()
input_ghz = tk.Entry()
input_ghz.pack()

label_ram = tk.Label(text= 'Memória Ram')
label_ram.pack()
input_ram = tk.Entry()
input_ram.pack()

label_storage = tk.Label(text= 'Armazenamento')
label_storage.pack()
input_storage = tk.Entry()
input_storage.pack()

label_os = tk.Label(text= 'Sistema Operacional')
label_os.pack()
input_os = tk.Entry()
input_os.pack()

label_price = tk.Label(text= "Preço")
label_price.pack()
input_price = tk.Entry()
input_price.pack()

janela.mainloop()

#GHz_processador, memoria_RAM, armazenamento, sistema_operacional, preco