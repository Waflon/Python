import os
os.system("cls")

num = int(input("Ingrese un valor para n: "))

if num == 0:
    print("Numero no valido")
elif num < 0:
    print("Numero negativo")
else:
    print("Numero positivo")