import funciones4final
dscto=0
porc=0
bono_ord=0
quinta=0

nombre = input ("Ingrese su nombre: ")
sueldo = int(input("Ingrese el valor de su sueldo bruto mensual: "))
print()
while True:
    sistema_pension = input("Eliga el sistema de pensiones al que pertenece ONP/AFP: ")
    if sistema_pension=="AFP" or sistema_pension=="afp" or sistema_pension=="Afp":
        while True:
            porc = float(input("Ingrese el porcentaje del AFP: "))
            if porc<11:
                print("Por ley general el porcentaje debe ser 11% o mas. Vuelva a ingresar")                
            else:
                dscto = funciones4final.AFP(sueldo,porc)
                break
        break
    elif sistema_pension=="ONP" or sistema_pension=="onp" or sistema_pension=="Onp":
        porc = 0.13
        dscto = sueldo*porc
        print("El porcentaje a descontar por ONP es el 13%")
        break
    else:
        print("Escriba correctamente.")
print()
while True:
    extra = input("Cuenta con algun bono ordinario aparte de su sueldo? s/n: ")
    if extra=="s" or extra=="S" or extra=="si":
        bono_ord = int(input("Inserte el valor: "))
        break
    elif extra=="N" or extra=="n":
        bono_ord = 0
        break
    else:
        print("Vuelva a ingresar.")

print()
print(f"Estimado Sr(a) {nombre} \nDe acuerdo a su remuneracion neta, usted cuenta con los siguientes descuentos: ")
print(f"\tDescuento por {sistema_pension} de S/.{dscto}")
if sueldo>2150:
    quinta = funciones4final.i_5c(sueldo,bono_ord)
    print(f"\tDescuento por renta de 5ta categoria de S/.{quinta}")
else:
    print(f"Debido a que su sueldo mensual de S/.{sueldo} es menor al estipulado (S/.2150), no le corresponde renta de 5ta categoria")
total = sueldo-dscto-quinta
print(f"Su Remuneracion neta mensual es {total}")