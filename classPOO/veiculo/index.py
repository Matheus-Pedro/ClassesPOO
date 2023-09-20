import tkinter as tk

window = tk.Tk()

window.geometry('300x500')
window.resizable(True, True)
window.title('Veículo')

label_brand = tk.Label(text='Marca')
label_brand.pack()
input_brand = tk.Entry()
input_brand.pack()

label_name = tk.Label(text='Nome')
label_name.pack()
input_name = tk.Entry()
input_name.pack()

label_motor = tk.Label(text='Motor')
label_motor.pack()
input_motor = tk.Entry()
input_motor.pack()

label_horses = tk.Label(text='Cavalos')
label_horses.pack()
input_horses = tk.Entry()
input_horses.pack()

label_zero_to_hundred = tk.Label(text='Zero a cem (segundos)')
label_zero_to_hundred.pack()
input_zero_to_hundred = tk.Entry()
input_zero_to_hundred.pack()

label_year = tk.Label(text='Ano de lançamento')
label_year.pack()
input_year = tk.Entry()
input_year.pack()

label_km = tk.Label(text='Quilometragem')
label_km.pack()
input_km = tk.Entry()
input_km.pack()

label_carroceria = tk.Label(text='Carroceria')
label_carroceria.pack()
input_carroceria = tk.Entry()
input_carroceria.pack()

label_cambio = tk.Label(text='Cambio')
label_cambio.pack()
input_cambio = tk.Entry()
input_cambio.pack()

label_combustivel = tk.Label(text='Combustível')
label_combustivel.pack()
input_combustivel = tk.Entry()
input_combustivel.pack()

window.mainloop()
