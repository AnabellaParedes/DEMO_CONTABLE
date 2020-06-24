#sueldom = sueldo mensual
#sueldoa = sueldo anual
#m = n meses
#g = grati
#mes_i = mes de inicio
#mes_f =  mes de salida
#anio_i = anio de inicio
#anio_f = anio de salida

def conteo_meses(iniciomes,finmes,inicioanio,finalanio):
    
    mes_i=iniciomes
    mes_f=finmes
    anio_i=inicioanio
    anio_f=finalanio

    #total num de meses
    if mes_f>=mes_i:
        if anio_f==anio_i:
            m=(mes_f-mes_i)+1
            
        elif anio_f>anio_i:
            m=(mes_f-mes_i)+12*(anio_f-anio_i)+1
    else:
        m=12-mes_i+mes_f+1
    return m

def grati(sueldom,m):   #para costo laboral
    g = (sueldom/6)*(m)
    return g

def bono(gratificacion):   #para costo y liquidacion
    bono = gratificacion*0.09
    return bono