numero_secreto = 7
for intentos in range(10):  # Desde 0 hasta 4
    print(f"Te quedan {10-intentos} intentos")
    numero = int(input("Digite un numero del 1 al 10: "))
    if numero == numero_secreto:
        print("Escogiste el numero correcto")
        break
    elif numero > numero_secreto:
        print("el numero es menor")
    else:
        print("el numero es mayor")