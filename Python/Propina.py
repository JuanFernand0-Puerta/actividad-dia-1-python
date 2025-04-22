cuenta=float(input("ingrese el monto de la cuenta"))

porcentaje_propina =float(input ("ingrese el porcentaje de la propina que quiere dejar: (10, 15, 20)"))
if porcentaje_propina not in (10,15,20):
    print("ingrese otro porcentaje valido")
else:   
    propina= cuenta * (porcentaje_propina/ 100)
    total = cuenta + propina 

print ("la propina es :", propina)
print ("el total de que debe pagar es ",total )