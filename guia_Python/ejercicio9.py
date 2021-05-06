import os
os.system("cls")

iva = 0.0
total = 0.0


precio = int(input("Ingrese precio del producto: "))

iva = precio * 0.19

total = precio + iva

print ("El total a pagar por :", total)
print ("El total a pagar por iva es de :", iva)