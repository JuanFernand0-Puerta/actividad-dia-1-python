peso= float (input ("digite su peso"))
altura= float (input("digite su altura"))

IMC = peso / (altura ** 2)
      
if IMC<18.5:
    print ("Bajo peso")
elif IMC<24.9:
    print("Normal")
elif IMC >=24.9 and IMC < 29.9:
    print ("Sobrepeso")
else:
     print ("obesidad")