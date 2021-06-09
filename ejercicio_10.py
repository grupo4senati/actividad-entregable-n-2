horas = int(input("Numero de horas trabajadas: "))
turno = input("Turno de trabajo (mañana, tarde, noche): ")
tarifa=37
if turno == "tarde":
    tarifa+=1.20
    sueldo = horas*tarifa
    print(f"El sueldo bruto de la tarde es {sueldo}")
elif turno == "noche":
    tarifa+=1.50
    sueldo = horas*tarifa
    if (sueldo >= 2000 and sueldo<=5000):
        descuento1 = (15/100)*sueldo
        sueldo=sueldo-descuento1
        print(f"El sueldo bruto de la noche menos el 15% es {sueldo}")
    elif (sueldo >= 8000 and sueldo<=10000):
        descuento2 = (17/100)*sueldo
        sueldo=sueldo-descuento2
        print(f"El sueldo bruto de la noche menos el 17% es {sueldo}")
    else:
        print("El sueldo bruto de la noche es " ,sueldo)
else:
    tarifa+=0
    sueldo = horas*tarifa
    print(f"El sueldo bruto de la mañana es {sueldo}")



