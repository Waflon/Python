import os
os.system("cls")

c=0

try:
    #edad= int(input("Ingrese su edad: 55"))
    #esto sirve para poner todo dentro de el int input
    edad= int(input(f"Ingrese la  edad: {c}"))
    print("Su edad es: ", edad)
    print("edad es del tipo: ", type(edad))
except ValueError:
    print ("error weon")