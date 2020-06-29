from tkinter import *
import funciones4final
from tkinter import ttk
from tkinter import messagebox

class Aplicacion():
    def __init__(self):
        self.NETO = Tk()
        self.NETO.title("REMUNERACION NETA")
        self.NETO.geometry("490x650")

        #variables de control
        self.nombre = StringVar()
        self.SueldoMensual = IntVar() 
        self.SistemaPensiones = StringVar()   #value = 'a'
        self.porcentaje = DoubleVar()
        self.total = StringVar()
        
        # Define trazas con variables de control de los widgets Entry()
        # para detectar cambios en los datos. Si se producen cambios
        # se llama a la función 'self.calcular' para validación y para
        # calcular importe a pagar
        
        # Llama a función para validar y calcular
        
        self.calcular()
        
        # Carga imagen para asociar a widget Label()

        photo = PhotoImage(file='salario-mínimo.png')

        #etiquetas y mas
        self.imagen1 = ttk.Label(self.NETO, image=photo, anchor="center")
        self.etiq1 = ttk.Label(self.NETO, text="Ingrese su nombre:")   #'Helvetica 18 bold'
        self.n = ttk.Entry(self.NETO, textvariable=self.nombre, width=20)

        self.etiq2 = ttk.Label(self.NETO, text="Ingrese Sueldo Mensual Bruto:")
        self.s = ttk.Entry(self.NETO, textvariable=self.SueldoMensual, width=20)

        self.etiq3 = ttk.Label(self.NETO, text="Eliga Sistema de Pensiones:")
        self.sp1 = ttk.Radiobutton(self.NETO, text='AFP -> Administradoras de Fondos de Pensiones', variable=self.SistemaPensiones, value='a')
        self.sp2 = ttk.Radiobutton(self.NETO, text='ONP -> Oficina de Normalización Previsional', variable=self.SistemaPensiones, value='o')
        
        self.etiq4 = ttk.Label(self.NETO, text="Si elige ONP, el porcentaje establecido es 13%")
        self.etiq5 = ttk.Label(self.NETO, text="Ingrese tasa por el sistema de pension (Sin el %)")
        self.porcentaje = ttk.Entry(self.NETO, textvariable=self.porcentaje, width=10)
        self.etiq6 = ttk.Label(self.NETO, text="Informacion:")        
        self.etiq7 = ttk.Label(self.NETO, textvariable=self.total, foreground="yellow", background="black", borderwidth=5, relief="sunken", anchor="e") 

        self.separ1 = ttk.Separator(self.NETO, orient=HORIZONTAL)
        
        self.boton1 = ttk.Button(self.NETO, text="Calcular", command=self.calcular)
        self.boton3 = ttk.Button(self.NETO, text="Info", command=self.Informacion)
        self.boton4 = ttk.Button(self.NETO, text="Borrar", command=self.Borrar)
        self.boton2 = ttk.Button(self.NETO, text="Salir", command=self.NETO.destroy)
        

        #anadiendo
        self.imagen1.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.etiq1.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.n.pack(side=TOP, fill=X, expand=True, padx=20, pady=5)

        self.etiq2.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.s.pack(side=TOP, fill=X, expand=True, padx=20, pady=5)

        self.etiq3.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.sp1.pack(side=TOP, fill=BOTH, expand=True, padx=20, pady=5)
        self.sp2.pack(side=TOP, fill=BOTH, expand=True, padx=20, pady=5)
        self.etiq4.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.etiq5.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.porcentaje.pack(side=TOP, fill=X, expand=True, padx=20, pady=5)

        self.etiq6.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.etiq7.pack(side=TOP, fill=BOTH, expand=True, padx=20, pady=5)

        self.separ1.pack(side=TOP, fill=BOTH, expand=True, padx=5, pady=5)
        self.boton1.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.boton3.pack(side=LEFT, fill=BOTH, expand=True, padx=10, pady=10)
        self.boton2.pack(side=RIGHT, fill=BOTH, expand=True, padx=10, pady=10)
        self.boton4.pack(side=RIGHT, fill=BOTH, expand=True, padx=10, pady=10)
        
        

        #ventana abierta
        self.NETO.mainloop()

    def calcular(self, *args):
        #Función para validar datos y calcular el sueldo neto
        error_dato = False
        total = 0
        try:
            nombre = str(self.nombre.get())
            sueldo = float(self.SueldoMensual.get())
            porcentaje = float(self.porcentaje.get())
            AFP = funciones4final.AFP(sueldo,porcentaje)
            quinta = funciones4final.i_5c(sueldo,0)
            
        except:
            error_dato = True

        if not error_dato:
            #if sueldo>2150:
            self.total.set("")
            if self.SistemaPensiones.get() == "a":
                if porcentaje<11:
                    self.total.set("RECORDAR. La tasa minima para el AFP es 11%")
                else:
                    total = sueldo - AFP - quinta
                    texto = f"Estimado Sr(a) {nombre} \nDe acuerdo a su remuneracion neta, usted cuenta con los siguientes descuentos: \n\tDescuento por AFP de S/.{AFP} \n\tDescuento por renta de 5ta categoria de S/.{quinta} \nSu Remuneracion neta mensual es {total}"
                    self.total.set(texto) 

            elif self.SistemaPensiones.get() == "o":
                if porcentaje != 13:
                    self.total.set("ERROR. La tasa para la ONP es 13%")
                else:
                    onp = sueldo*0.13
                    total = sueldo - onp - quinta
                    texto = f"Estimado Sr(a) {nombre} \nDe acuerdo a su remuneracion neta, usted cuenta con los siguientes descuentos: \n\tDescuento por ONP de S/.{onp} \n\tDescuento por renta de 5ta categoria de S/.{quinta} \nSu Remuneracion neta mensual es {total}"
                    self.total.set(texto)

        else:
            self.total.set("ERROR")

    def Informacion(self):
        messagebox.showinfo("Recuerde...", "<1> El valor de la tasa de la ONP es 13% \n<2> Si tiene un sueldo menor a 2150 no paga Impuesto de 5ta categoria \n<3> La tasa minima del AFP es 11%")
    
    def Borrar(self):
        self.nombre.set("")
        self.SueldoMensual.set("")
        self.porcentaje.set("")

def main():
    Aplicacion()
    return 0

if __name__ == "__main__":
    main()