def suma(uno,dos):
    print(uno+dos)
def resta(uno,dos):
    print(uno-dos)
def multiplica(uno,dos):
    print(uno*dos)
def divide(uno,dos):
    print(uno/dos)


num1=float(input("Ingrese el digito 1: "))
num2=float(input("Ingrese el digito 2: "))

operacion=input("que operacion desea hacer: (suma,resta,multiplica,divide) ")

if operacion == "suma":
    suma(num1,num2)
elif operacion == "resta":
    resta(num1,num2)
elif operacion == "multiplica":
    multiplica(num1,num2)
elif operacion == "divide":
    divide(num1,num2)
else:
    print("la operacion es incorrecta")
