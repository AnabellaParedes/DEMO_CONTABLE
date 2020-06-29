import funciones4final

fecha_inicio_anio = -1
fecha_inicio_mes = -1
fecha_salida_anio = -1
fecha_salida_mes = -1

nombre = input ("Ingrese su nombre: ")
sueldo = int(input("Ingrese el valor de su sueldo mensual: "))
print()
print("Ingrese fecha de inicio (01/xx/xxxx): ")
while True:
    if not (0<fecha_inicio_mes<=12 and fecha_inicio_anio>=2000):
        fecha_inicio_mes = int(input("Mes: "))
        fecha_inicio_anio = int(input("Anio: "))
    else:
        break
print("Ingrese fecha de salida (30/xx/xxxx): ")
while True:
    if not (0<fecha_salida_mes<=12 and fecha_salida_anio>=2000):
        fecha_salida_mes = int(input("Mes: "))
        fecha_salida_anio = int(input("Anio: "))
    else:
        break
meses = funciones4final.conteo_meses(fecha_inicio_mes,fecha_salida_mes,fecha_inicio_anio,fecha_salida_anio)
vacaciones = funciones4final.vaca(sueldo,meses)
grati_trunca = funciones4final.grati_trunca(sueldo,fecha_inicio_mes,fecha_salida_mes,fecha_inicio_anio,fecha_salida_anio)
bono_ley = funciones4final.bono(grati_trunca)
cts_trunca = funciones4final.CTS_trunca(sueldo,fecha_inicio_mes,fecha_salida_mes,fecha_inicio_anio,fecha_salida_anio)

liquidacion = vacaciones+grati_trunca+bono_ley+cts_trunca

print()
print(f"Estimado Sr(a) {nombre} \nDe acuerdo a su fecha de ingreso y salida, su liquidacion es la siguiente: ")
print(f"\tPago por Vacaciones de S/.{vacaciones}")
print(f"\tPago por Gratificacion de S/.{grati_trunca}")
print(f"\tPago por Bono ley de S/.{bono_ley}")
print(f"\tPago por Compensacion por tiempo de trabajo CTS de S/.{cts_trunca}")
print(f"Su liquidacion es por el total de S/.{round(liquidacion,2)}")