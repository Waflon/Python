import os
os.system("cls")
c = 1;
entrada = 3500
cantidad = int(input("Ingrese cuantas entradas desea comprar: "))

while (c <= cantidad):
    #upper lleva el valor a solo letras mayusculas
    c+=1
    tipo = input(f"Ingrese tipo de persona para entrada {c}: (N.A.T): ").upper()
    if (tipo == "N"):
        total += 1500
    elif(tipo == "A"):
        total += 3500
    elif(tipo == "T"):
        total += 1000
    else:
        print ("Error, solo debe ingresar valores")
        c -= 1



print (f"El total a pagar por {num} entradas, será de :", total )