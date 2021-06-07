persona1 = int(input("Cuanto dinero va a depositar: "))
persona2 = int(input("Cuanto dinero va a depositar: "))
persona3 = int(input("Cuanto dinero va a depositar: "))

sumatoria= (persona1+persona2+persona3)
print("La cantidad total sumada de dinero es: "+str(sumatoria))

print("La primer persona deposito: "+str((persona1/sumatoria)*100)+" %")
print("La segunda persona deposito: "+str((persona2/sumatoria)*100)+" %")
print("La tercer persona  deposito: "+str((persona3/sumatoria)*100)+" %")

