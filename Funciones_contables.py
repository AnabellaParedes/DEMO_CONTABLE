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

def grati_trunca(sueldom,mes_i,mes_f):   #para liquidacion
    if mes_f==12 or mes_i==12:
        mes_f = mes_f-1
        mes_i = mes_i-1
    a=0
    if 1<=mes_f<=6 and 6<mes_i<=11:
        a = mes_f
    elif 1<=mes_i<=6 and 6<mes_f<=11:
        a = (mes_f-7)+1
    elif 1<=mes_f<=6 and 1<=mes_i<=6:
        a = mes_f-mes_i+1
    elif 6<=mes_f<=11 and 6<=mes_i<=11: 
        a = mes_f-mes_i+1 

    gratitrunca=(sueldom/6)*a
    return gratitrunca   

def vaca(sueldom,m):    #para costo laboral y liquidacion
    vt = (sueldom/12)*(m)
    return vt

def CTS(sueldom,m):        #para costo
    cts = ((sueldom+(sueldom+sueldom*0.09)/6)/12)*m
    return cts

def CTS_trunca(sueldom,mes_i,mes_f):     #para liquidacion
    b=0
    if (11<=mes_f<=12 or 1<=mes_f<=4) and 5<=mes_i<=10:
        b = (mes_f-11)+1
    elif (11<=mes_i<=12 or 1<=mes_i<=4) and 5<=mes_f<=10:
        b = (mes_f-5)+1
    elif (11<=mes_f<=12 or 1<=mes_f<=4) and (11<=mes_i<=12 or 1<=mes_i<=4):
        b = (mes_f-mes_i)+1
    elif 5<=mes_i<=10 and 5<=mes_f<=10:
        b = (mes_f-mes_i)+1
    
    ctstrunca = ((sueldom+(sueldom+sueldom*0.09)/6)/12)*b
    return ctstrunca
