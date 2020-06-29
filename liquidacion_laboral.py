from tkinter import *
import funciones4final
from tkinter import ttk
from tkinter import messagebox

class Aplicacion_1():
    def __init__(self):
        self.LIQ = Tk()
        self.LIQ.title("LIQUIDACION")
        self.LIQ.geometry("440x700")
        self.LIQ.resizable(0,0)

        #variables de control
        self.nombre = StringVar()
        self.SueldoMensual = DoubleVar(value=0) 
        self.mes_inicio = IntVar()   
        self.mes_salida = IntVar()   
        self.anio_inicio = IntVar()
        self.anio_salida = IntVar()
        self.total = StringVar()

        # Llama a función para validar y calcular
        
        self.calcular1()
        
        # Carga imagen para asociar a widget Label()

        photo1 = PhotoImage(file='dinero.png')

        self.imagen = ttk.Label(self.LIQ, image=photo1, anchor="center")
        self.etiq1 = ttk.Label(self.LIQ, text="Ingrese su nombre:")   #'Helvetica 18 bold'
        self.n = ttk.Entry(self.LIQ, textvariable=self.nombre, width=20)

        self.etiq2 = ttk.Label(self.LIQ, text="Ingrese Sueldo Mensual:")
        self.s = ttk.Entry(self.LIQ, textvariable=self.SueldoMensual, width=20)

        self.etiq3 = ttk.Label(self.LIQ, text="Ingrese Fecha de Ingreso: 01/XX/XXXX")
        self.etiq4 = ttk.Label(self.LIQ, text="Mes de Ingreso")  #.grid(row=0, sticky=W)
        self.etiq5 = ttk.Label(self.LIQ, text="Año de Ingreso")   #.grid(row=0, sticky=E)
        self.mes_i = Spinbox(self.LIQ, from_=1, to=12, wrap=True, textvariable=self.mes_inicio, state='readonly') #, command=self.calcular
        self.anio_i = ttk.Entry(self.LIQ, textvariable=self.anio_inicio, width=6)

        self.etiq6 = ttk.Label(self.LIQ, text="Ingrese Fecha de Salida: 30/XX/XXXX")
        self.etiq7 = ttk.Label(self.LIQ, text="Mes de Salida")   #.grid(row=0, sticky=W)
        self.etiq8 = ttk.Label(self.LIQ, text="Año de Salida")    #.grid(row=0, sticky=E)
        self.mes_s = Spinbox(self.LIQ, from_=1, to=12, wrap=True, textvariable=self.mes_salida, state='readonly')   #, command=self.calcular
        self.anio_s = ttk.Entry(self.LIQ, textvariable=self.anio_salida, width=6)

        self.etiq9 = ttk.Label(self.LIQ, text="RESULTADOS")
        self.etiq10 = ttk.Label(self.LIQ, textvariable=self.total, foreground="yellow", background="black", borderwidth=5, relief="sunken", anchor="e")

       
        #Botones a usar
        self.boton1 = ttk.Button(self.LIQ, text="Calcular", command=self.calcular1) 
        #self.boton3 = ttk.Button(self.LIQ, text="Info")   #, command=self.Informacion
        self.boton4 = ttk.Button(self.LIQ, text="Borrar", command = self.Borrar)
        self.boton2 = ttk.Button(self.LIQ, text="Salir", command = self.LIQ.destroy)  



        self.imagen.grid(row=1, column=0, columnspan=2, rowspan=2, sticky=W+E+N+S, padx=2, pady=2)
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

       
        self.boton2.grid(row=45, column=1, padx=5, pady=5)
        self.boton4.grid(row=45, column=0, padx=5, pady=5)

        #ventana abierta
        self.LIQ.mainloop()

    def calcular1(self, *args):
        #Función para validar datos y calcular la liquidacion neta
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
            
            if meses==0:    #Esto corresponde a la validacion en la funcion de conteo de meses
                self.total.set("Aun no hacemos viajes en el tiempo                                                                    ")
            else:
                v = round(funciones4final.vaca(sueldo,meses),2)
                grati = round(funciones4final.grati_trunca(sueldo,mes_inicio,mes_salida,anio_inicio,anio_salida),2)
                bono = round(funciones4final.bono(grati),2)
                cts = round(funciones4final.CTS_trunca(sueldo,mes_inicio,mes_salida,anio_inicio,anio_salida),2)
                total = v+grati+bono+cts
                texto = f"Estimado Sr(a) {nombre} \nDe acuerdo a su fecha de ingreso y salida, su liquidacion es la siguiente: \n\tPago por Vacaciones de S/.{v} \n\tPago por Gratificacion de S/.{grati} \n\tPago por Bono ley de S/.{bono} \n\tPago por Compensacion por tiempo de trabajo CTS de S/.{cts} \nSu liquidacion es por el total de S/.{round(total,2)}"
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
    Aplicacion_1()
    return 0

if __name__ == "__main__":
    main()