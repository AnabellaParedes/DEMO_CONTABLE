import funciones4final

fecha_inicio_anio = -1
fecha_inicio_mes = -1
fecha_salida_anio = -1
fecha_salida_mes = -1

nombre = input ("Ingrese su nombre: ")
trabajadores = int(input("A cuantos trabajadores desea contratar: "))
sueldo = int(input("Cual es el sueldo mensual que le pagara  a los trabajadores: "))
print()
print("Ingrese fecha de inicio (01/xx/xxxx): ")
while True:
    if not (0<fecha_inicio_mes<=12 and fecha_inicio_anio>=2000):
        fecha_inicio_mes = int(input("Mes: "))
        fecha_inicio_anio = int(input("Anio: "))
    else:
        break
print("Ingrese fecha de inicio (30/xx/xxxx): ")
while True:
    if not (0<fecha_salida_mes<=12 and fecha_salida_anio>=2000):
        fecha_salida_mes = int(input("Mes: "))
        fecha_salida_anio = int(input("Anio: "))
    else:
        break
meses = funciones4final.conteo_meses(fecha_inicio_mes,fecha_salida_mes,fecha_inicio_anio,fecha_salida_anio)
vacaciones = funciones4final.vaca(sueldo,meses)
gratificacion = funciones4final.grati(sueldo,meses)
bono_ley = funciones4final.bono(gratificacion)
cts = funciones4final.CTS(sueldo,meses)
sueldo_total= sueldo*meses
essalud = funciones4final.ESSALUD(sueldo,meses)
costo_laboral = vacaciones+gratificacion+bono_ley+cts+sueldo_total+essalud

print()
print(f"Estimado Sr(a) {nombre} \nDe acuerdo al total de meses del contrato del trabajador, el costo laboral es el siguiente: ")
print(f"\tCosto por Vacaciones de S/.{vacaciones}")
print(f"\tCosto por Gratificacion de S/.{gratificacion}")
print(f"\tCosto por Bono ley de S/.{bono_ley}")
print(f"\tCosto por Compensacion por tiempo de trabajo CTS de S/.{cts}")
print(f"\tCosto por Sueldo por los {meses} meses es de S/.{sueldo_total}")
print(f"\tCosto por seguro social ESSALUD de S/.{essalud}")
print(f"El costo es por el total de S/.{round(costo_laboral,2)}")
if trabajadores==1:
    print(f"\tPor el contrato de un solo trabajador, el costo laboral es el mismo: S/.{round(costo_laboral,2)}")
elif trabajadores>1:
    print(f"\tPor el contrato de {trabajadores} trabajadores, el costo laboral es S/.{round(costo_laboral*trabajadores,2)}")