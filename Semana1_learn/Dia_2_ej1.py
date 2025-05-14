num1=int(input("Digite numero1: "))
num2=int(input("Digite numero2: "))
num3=int(input("digite numero3: "))

if num1 < num2 and num1 < num3:
    print("El numero 1 es menor")
elif num2 < num1 and num2 < num3:
    print("El numero 2 es menor")
elif num3 < num1 and num3 < num2:
    print("El numero 3 es menor")