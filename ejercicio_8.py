dni=input("Ingrese el DNI: ")

contador = 0
for x in dni:
    contador+=1


if contador > 8:
    print("Error: DNI contiene mas de 8 caracteres")
elif contador < 8:
    print("Error: DNI contiene menos de 8 caracteres")
else:
    print("El DNI es correcto")

    
