import tkinter as tk
from tkinter import ttk

window = tk.Tk()

window.geometry('300x300')
window.resizable(True, True)
window.title('Pagamento')

label_formofpayment = tk.Label(text='Forma de pagamento')
label_formofpayment.pack()
input_formofpayment = tk.Entry()
input_formofpayment.pack()

label_payee = tk.Label(text='Sacador')
label_payee.pack()
input_payee = tk.Entry()
input_payee.pack()

label_payer = tk.Label(text='Sacado')
label_payer.pack()
input_payer = tk.Entry()
input_payer.pack()

label_date_hdma = tk.Label(text= 'Data de pagamento (Hora, dia, mês e ano)')
label_date_hdma.pack()
input_date_hdma = tk.Entry()
input_date_hdma.pack()
#forma_pagamento, sacador, sacado, data_hdma, valor

label_value = tk.Label(text= 'Valor')
label_value.pack()
input_value = tk.Entry()
input_value.pack()

window.mainloop()
