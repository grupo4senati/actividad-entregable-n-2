nombre = input("Ingrese su nombre: ")
horas= int(input("Ingrese sus horas trabajadas: "))
salario= int(input("Ingrese el salario por hora: "))
print("su nombre es {nombre}, ha trabajado {horas} horas, y su salario por hora es de {salario} soles")
sueldo = (horas * salario)
print("Su sueldo final es de {sueldo} soles")
sueldoAumentado= (15/100*sueldo)
sueltoTotal = sueldoAumentado + sueldo


