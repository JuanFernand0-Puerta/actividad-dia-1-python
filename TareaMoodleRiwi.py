print ("┏━━━━━━━━━━━━━━━━━┓┏━━━━━━━━━━━━━━━━━┓┏━━━━━━━━━━━━━━━━━┓")
print ("                         VALIDACION  DE  PRODUCTO        ")
print ("┗━━━━━━━━━━━━━━━━━┛┗━━━━━━━━━━━━━━━━━┛┗━━━━━━━━━━━━━━━━━┛")






while True:
    try:
        producto=  str (input("Dime el nombre del producto que quieres"))
        
        if producto.isalpha():
            break
        else:    
            print("Debes ingresar un producto valido")
        
    except ValueError:  
        print("Ingrese un producto valido")

while True:
    try:
        cantidad = int(input("Dime cuantos productos llevarás"))
        if cantidad < 0:
            print("Debe de agregar una cantidad de producto que no sea 0 o un valor negativo")
        else:
            break  # Terminar el bucle si la cantidad es válida
    except ValueError:
        print("Dato invalido")
  

while True:
    try:
        porcentaje= int (input("Que porcentaje se le aplicara al producto, (0,100%)"))
        if porcentaje >=1 and porcentaje <= 100 or porcentaje ==0:
            print ("El porcentaje es:",porcentaje)
            break
        else:
            print("El porcentaje debe estar en un rango 0% , 100%")
    except ValueError:
        print("Dato invalido")

while True:
    try:
        precio= float (input("Dime el precio por unidad que desees"))
        if precio > 0:
            break
        print("ingrese un precio mayor que 0")
    
    except ValueError:
        print("Debes de ingresar un valor que sea valido")

    total=float
        



print("´´"**30)
print("factura")
print("´´"**30)

total= precio*porcentaje/100
print("el total de la cuenta es: ",total)



          




    
    





