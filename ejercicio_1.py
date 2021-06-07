print("Ejercicio N°1")
print("==========Calcular Promedio==========")


cantidad=int(input("INGRESE EL NUMERO DE NOTAS: "))

contador=1
sumatoria=0


while contador <= cantidad:
    
    nota = int(input("INGRESE NOTA: "))
    sumatoria += nota

    contador+=1

print(int(sumatoria / cantidad))




print("-----------------Gracias por utilizar el programa-----------------")











