import costo_laboral
import sueldo_neto
import liquidacion_laboral
from tkinter import *
import funciones4final
from tkinter import ttk

#sueldo = sueldo_neto.Aplicacion()
#liqui = liquidacion_laboral.Aplicacion_1()
#costo = costo_laboral.Aplicacion_2()

derived = Tk()
derived.title("DEMO TRIBUTARIO")
derived.geometry("490x300")



a = ttk.Button(derived, text="SUELDO NETO", command=sueldo_neto.Aplicacion)
b = ttk.Button(derived, text="LIQUIDACION", command=liquidacion_laboral.Aplicacion_1)
c = ttk.Button(derived, text="COSTO LABORAL", command=costo_laboral.Aplicacion_2)

a.pack(side=LEFT, fill=X, expand=True, padx=10, pady=10)
b.pack(side=RIGHT, fill=X, expand=True, padx=10, pady=10)
c.pack(side=RIGHT, fill=X, expand=True, padx=10, pady=10)

derived.mainloop()  