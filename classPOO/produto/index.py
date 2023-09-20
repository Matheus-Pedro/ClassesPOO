import tkinter as tk
from tkinter import ttk

window = tk.Tk()

window.geometry('300x400')
window.resizable(True, True)
window.title('Produto')

label_name = tk.Label(text='Nome')
label_name.pack()
input_name = tk.Entry()
input_name.pack()

label_purchase = tk.Label(text='Preço de compra')
label_purchase.pack()
input_purchase = tk.Entry()
input_purchase.pack()

label_sale = tk.Label(text='Preço de venda')
label_sale.pack()
input_sale = tk.Entry()
input_sale.pack()

label_product_stock = tk.Label(text='Quantidade em estoque')
label_product_stock.pack()
input_product_stock = tk.Entry()
input_product_stock.pack()

label_warrantly = tk.Label(text='Garantia')
label_warrantly.pack()
input_warrantly = tk.Entry()
input_warrantly.pack()

window.mainloop()
