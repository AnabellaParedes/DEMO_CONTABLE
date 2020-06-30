import costo_laboral
import sueldo_neto
import liquidacion_laboral
from tkinter import *
import funciones4final
from tkinter import ttk
import os


derived = Tk()
derived.title("DEMO TRIBUTARIO")
derived.geometry("490x250")
derived.config(bg="light grey")

def b1():
    os.system('sueldo_neto.py')
def b2():
    os.system('liquidacion_laboral.py')
def b3():
    os.system('costo_laboral.py')
    
etiq0 = ttk.Label(derived, text="DEMO CONTABLE", anchor="center", font = 'Helvetica 25 bold').place(x=108,y=40)
a = ttk.Button(derived, text="SUELDO NETO", command=b1).place(x=80,y=100)
b = ttk.Button(derived, text="LIQUIDACION", command=b2).place(x=200,y=100)
c = ttk.Button(derived, text="COSTO LABORAL", command=b3).place(x=320,y=100)
d = ttk.Button(derived, text = "SALIR", command = derived.destroy).place(x=200,y=160)


derived.mainloop()  