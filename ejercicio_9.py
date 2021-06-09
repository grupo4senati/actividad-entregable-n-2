dvd1={"salsa":56,"rock":63,"pop":87,"folclore":120.5}
dvd2={56:"salsa",63:"rock",87:"pop",120.5:"folclore"}
compras=0
montoTotal=0
contenedor=[]
generos=[]
saldo = int(input("Ingrese su saldo: "))
saldoInicial=saldo
if saldo<=0:
    print("su saldo es incorrecto")
else:
    while True:
        print("Saldo Inicial:",saldoInicial)
        print("Saldo disponible:",saldo)
        print( )
        print("MARCA       |  PRECIO UNITARIO")
        print("Salsa:      |   S/. 56.00")
        print("Rock:       |   S/. 63.00")
        print("Pop:        |   S/. S/. 87.00")
        print("Folclore:   |   S/. 120.50")
        print( )
        eleccion=input("Escoja el genero que mas le guste: ")
        print()
        print("PROCESANDO VAUCHER....................")
        if saldo >= dvd1[eleccion]:

            precioDisco = dvd2[eleccion]
            print()
            print("===========IMPORTE A PAGAR===========")
            print("Saldo Inicial:",saldoInicial)
            print("Saldo disponible:",saldo)
            print("Genero: "+str(dvds2[precioDisco]))
            print("Importe: "+str(dvds[eleccion]))
            print()
            

            reafirmacion = input("DESEA REALIZAR LA COMPRA? (SI / NO) ")


            if reafirmacion=="si":
                print()
                print()
                print("===========COMPRA SATISFACTORIA===========")
                saldo = (saldo - dvds[eleccion])
                print("Genero: "+str(dvd2[precioDisco]))
                print("Importe: "+str(dvd1[eleccion]))

                montoTotal = montoTotal+dvd1[eleccion]
                compras= compras+1
                generos.append(dvd1[eleccion])
                contenedor.append(dvd2[precioDisco])
                print("Detalles de la compra: ",contenedor)
        else:
            print( )
            print("No cuenta con el saldo suficiente para esta compra")
            print("Su saldo actual ",saldo," soles")
            print("Saldo Inicial:",saldoInicial)
            print("Saldo disponible:",saldo)

        if compras==4:
            print("Descuentos: !Usted accedio a un descuento de 6.0% por comprar mas de 3 productos!")
            descuento1 = (6/100)*montoTotal
            saldo=saldo+descuento1

        elif (compras >= 5 and compras<=10):
            print("Descuentos: !Usted accedio a un descuento de 8.0% por comprar mas de 5 productos!")
            descuento2 = (8/100)*montoTotal
            saldo=saldo+descuento2
        
        elif compras>10:
            print("Descuentos: !Usted accedio a un descuento de 10.2% por comprar mas de 10 productos!")
            descuento3 = (10.2/100)*montoTotal
            saldo=saldo+descuento3
        else:
            print("Descuentos: No cuenta con ningun descuento u cortesia")
        print("Compras Hechas: ",compras)
        print("Saldo Inicial:",saldoInicial)
        print("Saldo disponible:",saldo)
        print("EL MONTO TOTAL",montoTotal)
        posters=0
        if (generos.count(56)>3 and compras >=6):
            print("Enhorabuena, ganaste 1 poster por comprar 4 veces el mismo genero salsa")

        if (generos.count(63)>3 and compras >=6):
            print("Enhorabuena, ganaste 1 poster por comprar 4 veces el mismo genero rock")

        if (generos.count(87)>3 and compras >=6):
            print("Enhorabuena, ganaste 1 poster por comprar 4 veces el mismo genero pop")

        if (generos.count(120.5)>3 and compras >=6):
            print("Enhorabuena, ganaste 1 poster por comprar 4 veces el mismo genero floclore")

        
    



