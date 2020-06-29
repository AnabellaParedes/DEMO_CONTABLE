#sueldom = sueldo mensual
#sueldoa = sueldo anual
#m = n meses
#g = grati
#mes_i = mes de inicio
#mes_f =  mes de salida
#anio_i = anio de inicio
#anio_f = anio de salida

def conteo_meses(iniciomes,finmes,inicioanio,finalanio):
    #Se quiere determinar el numero de meses para los diferentes calculos en el programa
    #Se evalua de acuerdo al año y los meses, además valida que tenga sentido, por ejemplo
    #si es año final es menor al inicial, no tendría coherencia
    
    mes_i=iniciomes
    mes_f=finmes
    anio_i=inicioanio
    anio_f=finalanio

    #total num de meses
    if mes_f>=mes_i:                 #si el mes final es mayor, se tomara en cuenta los años para los calculos
        if anio_f==anio_i:           #si los años son iguales
            m=(mes_f-mes_i)+1   
        elif anio_f>anio_i:          #si el año final es el mayor
            m=(12-mes_i+mes_f+1)+12*(anio_f-anio_i-1)
        else:
            m=0                       #si el año inicial fuera mayor, el num de meses es 0 para validarlo mas adelante
    else:
        if anio_f>anio_i:             #en caso de que el año final sea mayor
            m=(12-mes_i+mes_f+1)+12*(anio_f-anio_i-1)
        else:
            m=0                       #si el año y mes inicial fueran mayores, el num de meses es 0 para validarlo mas adelante

    return m                          
def grati(sueldom,m):   #para costo laboral
    #Calcula el total de grati completo por el tiempo que se le va a contratar
    #Equivale a un sexto del sueldo mensual por lo meses que trabajará
    g = (sueldom/6)*(m)
    return g

def bono(gratificacion):   #para costo laboral y liquidacion
    #El bono ley siempre será el 9% de la gratificacion otorgada
    bono = gratificacion*0.09
    return bono

def grati_trunca(sueldom,mes_i,mes_f,anio_i,anio_f):   #para liquidacion
    #Esto corresponde al calculo de el monto que le faltaria cobrar al empleado luego de su renuncia
    #Esta evaluado con respecto a las fechas de pago:
    #Desde enero a junio, se cobra el 15 de julio
    #Desde julio y noviembre, se cobra el 15 de diciembre
    #Puede que a la persona le toque cobrar solo lo que trabajo despues de una fecha de pago, 
    #o cobrar una gratificación completa
    if mes_f==12 or mes_i==12:     #se valida hasta el mes de noviembre
        mes_f = mes_f-1
        mes_i = mes_i-1
    a=0
    if anio_i<anio_f:              #si es año final es mayor
        if 1<=mes_f<=6 and 6<mes_i<=11:          #los numeros representan los meses
            a = mes_f                            #ejemplo: 1 igual a enero
        elif 1<=mes_f<=6 and 1<=mes_i<=6:
            a = mes_f
        elif 6<=mes_f<=11 and 6<=mes_i<=11:
            a = mes_f-6
        elif 1<=mes_i<=6 and 6<mes_f<=11:
            a = mes_f-6
    elif anio_f==anio_i:           #si sucede en el mismo año
        if 1<=mes_f<=6 and 1<=mes_i<=6:
            a = mes_f-mes_i+1
        elif 6<=mes_f<=11 and 6<=mes_i<=11: 
            a = mes_f-mes_i+1 
        elif 1<=mes_i<=6 and 6<mes_f<=11:
            a = mes_f-6
        elif 1<=mes_f<=6 and 6<mes_i<=11:
            a = mes_f

    gratitrunca=(sueldom/6)*a              #Corresponde a 1/6 del sueldo por los meses que faltan cobrar
    return gratitrunca 

def vaca(sueldom,m):    #para costo laboral y liquidacion
    #Para calcular el monto de las vacaciones que te correponden en pago
    #Equivale a un doceavo del sueldo mensual por los meses que se trabaje
    vt = (sueldom/12)*(m)
    return vt

def CTS(sueldom,m):        #para costo
    #Por ser usado para calcular el costo de contratar recien a una persona, no se consideran los parametros
    #de pago. Entonces se calcularia con respecto al tiempo que diraria el contrato "m"
    #Equivale a un sueldo mas un sexto de la gratificacion, entre 12
    cts = ((sueldom+(sueldom+sueldom*0.09)/6)/12)*m
    return cts

def CTS_trunca(sueldom,mes_i,mes_f,anio_i,anio_f):     #para liquidacion
    #Corresponde al monto que le falta cobrar al empleado despues de su salida antes de tiempo
    #Esta compensacion por tiempo de trabajo se pagan en estos dias:
    #De noviembre a abril, el 15 de mayo
    #De mayo a octubre, el 15 de noviembre
    #Puede que a la persona le toque cobrar solo lo que trabajo despues de una fecha de pago, 
    #o cobrar una cts completa
    b=0
    if anio_i<anio_f:                            #si el año final es mayor
        if 1<=mes_f<=4 and 5<=mes_i<=10:    
            b = mes_f+2
        elif 11<=mes_i<=12 and 1<=mes_f<=4:
            b = mes_f+2
        elif 11<=mes_i<=12 and 5<=mes_f<=10:
            b = mes_f-4
        elif 1<=mes_f<=4 and 1<=mes_i<=4:
            b = mes_f+2
        elif 5<=mes_i<=10 and 5<=mes_f<=10:
            b = mes_f-4
        elif 11<=mes_f<=12 and 11<=mes_i<=12:
            b = mes_f-10
        elif 11<=mes_f<=12 and 5<=mes_i<=10:
            b = mes_f-10   
        elif 1<=mes_i<=4 and 5<=mes_f<=10:
            b = (mes_f-5)+1
        elif 1<=mes_i<=4 and 11<=mes_f<=12:
            b = mes_f-10
    
    elif anio_f==anio_i:                          #Si sucede todo en un mismo año
        if 1<=mes_f<=4 and 1<=mes_i<=4:           #los meses finales no pueden ser menores
            b = mes_f-mes_i+1
        elif 5<=mes_i<=10 and 5<=mes_f<=10:
            b = (mes_f-mes_i)+1
        elif 11<=mes_f<=12 and 11<=mes_i<=12:
            b = mes_f-mes_i+1
        elif 11<=mes_f<=12 and 5<=mes_i<=10:
            b = mes_f-10   
        elif 1<=mes_i<=4 and 5<=mes_f<=10:
            b = (mes_f-5)+1
        elif 1<=mes_i<=4 and 11<=mes_f<=12:
            b = mes_f-10
    
    ctstrunca = ((sueldom+(sueldom+sueldom*0.09)/6)/12)*b    #Corresponde a un sueldo mas 1/6 de la grati, entre 12
    return ctstrunca                                         #Por los meses que faltan cobrar

def i_5c(sueldom,bono_ord):     #para remuneracion neta
    if sueldom<2150:       #Cuando el sueldo sea menor a 2150, no existe impuesto de 5ta
        i_5c=0
    else:                              #Se realiza una proyeccion anual
        s = sueldom*12                 #Se calcula el sueldo en una año (por 12)
        grati = sueldom*2              #En el año se ganan dos gratis
        bono = grati*0.09              #El bono es el 9% de la grati
        proyeccion_1anio = s+grati+bono+bono_ord             
        renta_neta = proyeccion_1anio-30100      #se le resta 7UIT(UIT=4300soles)
        #tasas de impuesto
        i = renta_neta/4300
        if i>0 and i<=5:                        #Existen distintas categorias para pagar un %
            i_5c = (renta_neta*0.08)/12         #mientras se suba de categoria, se acumula el gasto hasta el nivel que llegues
        elif i>5 and i<=20:
            a = 21500
            i_5c = (1720+(renta_neta-a)*0.14)/12
        elif i>20 and i<=35:
            a = 86000
            i_5c = (10750+(renta_neta-a)*0.17)/12
        elif i>35 and i<=45:
            a = 150500
            i_5c = (21715+(renta_neta-a)*0.2)/12
        elif i>45:
            a = 193500
            i_5c = (30315+(renta_neta-a)*0.3)/12
    
    return round(i_5c,2)

def AFP(sueldom,porc):
    porc = porc/100
    AFP = sueldom*porc            #Se paga un impuesto por AFP
    return AFP

def ESSALUD(sueldom,m):       #para costo laboral
    #El seguro social corresponde al 9% del sueldo
    porc_estado = 0.09
    essalud = (sueldom*m)*porc_estado 
    return essalud
