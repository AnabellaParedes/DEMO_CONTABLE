from tkinter import *
import funciones4final
from tkinter import ttk
from tkinter import messagebox

class Aplicacion_2():
    def __init__(self):
        self.C= Tk()
        self.C.title("COSTO LABORAL")
        self.C.geometry("410x650")
        self.C.resizable(0,0)

        #variables de control
        self.nombre = StringVar()
        self.SueldoMensual = DoubleVar(value=0) 
        self.mes_inicio = IntVar()   #value=1
        self.mes_salida = IntVar()   #value=2
        self.anio_inicio = IntVar()
        self.anio_salida = IntVar()
        self.total = StringVar()

        # Llama a función para validar y calcular
        
        self.calcular2()
        

        self.etiq0 = ttk.Label(self.C, text="COSTO LABORAL", anchor="center", font = 'Helvetica 18 bold')
        self.etiq1 = ttk.Label(self.C, text="Ingrese su nombre:")   #'Helvetica 18 bold'
        self.n = ttk.Entry(self.C, textvariable=self.nombre, width=20)

        self.etiq2 = ttk.Label(self.C, text="Ingrese Sueldo a Pagar mensualmente:")
        self.s = ttk.Entry(self.C, textvariable=self.SueldoMensual, width=20)

        self.etiq3 = ttk.Label(self.C, text="Ingrese Fecha de Ingreso: 01/XX/XXXX")
        self.etiq4 = ttk.Label(self.C, text="Mes de Ingreso")  #.grid(row=0, sticky=W)
        self.etiq5 = ttk.Label(self.C, text="Año de Ingreso")   #.grid(row=0, sticky=E)
        self.mes_i = Spinbox(self.C, from_=1, to=12, wrap=True, textvariable=self.mes_inicio, state='readonly') #, command=self.calcular
        self.anio_i = ttk.Entry(self.C, textvariable=self.anio_inicio, width=6)

        self.etiq6 = ttk.Label(self.C, text="Ingrese Fecha Termino de contrato: 30/XX/XXXX")
        self.etiq7 = ttk.Label(self.C, text="Mes de Salida")   #.grid(row=0, sticky=W)
        self.etiq8 = ttk.Label(self.C, text="Año de Salida")    #.grid(row=0, sticky=E)
        self.mes_s = Spinbox(self.C, from_=1, to=12, wrap=True, textvariable=self.mes_salida, state='readonly')   #, command=self.calcular
        self.anio_s = ttk.Entry(self.C, textvariable=self.anio_salida, width=6)

        self.etiq9 = ttk.Label(self.C, text="RESULTADOS")
        self.etiq10 = ttk.Label(self.C, textvariable=self.total, foreground="yellow", background="black", borderwidth=5, relief="sunken", anchor="e")

        self.boton1 = ttk.Button(self.C, text="Calcular", command=self.calcular2)  #
        #self.boton3 = ttk.Button(self.LIQ, text="Info")   #, command=self.Informacion
        self.boton4 = ttk.Button(self.C, text="Borrar", command=self.Borrar) #
        self.boton2 = ttk.Button(self.C, text="Salir", command = self.C.destroy)  #


        self.etiq0.grid(row=1, column=0, columnspan=2, rowspan=2, sticky=W+E+N+S, padx=2, pady=2)
        self.etiq1.grid(row=3, column=0, columnspan=4, padx=5, pady=5)
        self.n.grid(row=4, column=0, columnspan=4, sticky=W+E+N+S, padx=20, pady=5)

        self.etiq2.grid(row=5, column=0, columnspan=4, padx=5, pady=5)
        self.s.grid(row=6, column=0, columnspan=4, sticky=W+E+N+S, padx=20, pady=5)

        self.etiq3.grid(row=7, column=0, columnspan=4, padx=7, pady=7)
        self.etiq4.grid(row=8, column=0, padx=5, pady=5)
        self.mes_i.grid(row=8, column=1, padx=5, pady=5)
        self.etiq5.grid(row=9, column=0, padx=10, pady=5)
        self.anio_i.grid(row=9, column=1, columnspan=4, padx=10, pady=5)

        self.etiq6.grid(row=10, column=0, columnspan=4, padx=7, pady=7)
        self.etiq7.grid(row=11, column=0, padx=10, pady=5)
        self.mes_s.grid(row=11, column=1)
        self.etiq8.grid(row=12, column=0, padx=10, pady=5)
        self.anio_s.grid(row=12, column=1, columnspan=4, padx=10, pady=5)

        self.boton1.grid(row=13, column=0, columnspan=4, padx=5, pady=5)
        self.etiq9.grid(row=14, column=0, columnspan=4, padx=10, pady=10)
        self.etiq10.grid(row=15, column=0, columnspan=3, rowspan=14, sticky=W+E+N+S, padx=5, pady=5, ipadx=10, ipady=20)

        #self.separ1.grid(row=39, column=0, columnspan=2)
        
        #self.boton3.pack(side=LEFT, fill=BOTH, expand=True, padx=10, pady=10)
        self.boton2.grid(row=45, column=1, padx=5, pady=5)
        self.boton4.grid(row=45, column=0, padx=5, pady=5)
        #ventana abierta
        self.C.mainloop()

    def calcular2(self, *args):
        #Función para validar datos y calcular el sueldo neto
        error_dato = False
        total = 0
        try:
            nombre = self.nombre.get()
            sueldo = float(self.SueldoMensual.get())
            mes_inicio = self.mes_inicio.get()
            mes_salida = self.mes_salida.get()
            anio_inicio = int(self.anio_inicio.get())
            anio_salida = int(self.anio_salida.get())
            meses = funciones4final.conteo_meses(mes_inicio,mes_salida,anio_inicio,anio_salida)
           
        except:
            error_dato = True
        
        if not error_dato and sueldo>0:
            self.total.set("                                                                    ")
            if meses==0:
                self.total.set("Aun no hacemos viajes en el tiempo                                                                    ")
            else:
                v = round(funciones4final.vaca(sueldo,meses),2)
                grati = round(funciones4final.grati(sueldo,meses),2)
                bono = round(funciones4final.bono(grati),2)
                cts = round(funciones4final.CTS(sueldo,meses),2)
                sueldo_total = sueldo*meses
                essalud = funciones4final.ESSALUD(sueldo,meses)
                total = v+grati+bono+cts+sueldo_total+essalud
                texto = f"Estimado Sr(a) {nombre} \nComo empleador, el costo laboral por los {meses} meses es el siguiente: \n\tPago por Vacaciones de S/.{v} \n\tPago por Gratificacion de S/.{grati} \n\tPago por Bono ley de S/.{bono} \n\tPago por Compensacion por tiempo de trabajo CTS de S/.{cts} \n\tCosto por Sueldo por los {meses} meses es de S/.{sueldo_total} \n\tCosto por seguro social ESSALUD de S/.{essalud} \nEl costo es por el total de S/.{round(total,2)}"
                self.total.set(texto)
        
        elif sueldo==0:
            self.total.set("Ingrese valores correspondientes--------------------------------------------------")
        else:
            self.total.set("ERROR-----------------------------------------------------------------------------")
        
    def Borrar(self):
        self.nombre.set("")
        self.SueldoMensual.set("")
        self.anio_inicio.set("")
        self.anio_salida.set("")
        self.mes_inicio.set(value = 1)
        self.mes_salida.set(value = 1) 

def main():
    Aplicacion_2()
    return 0

if __name__ == "__main__":
    main()