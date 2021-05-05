import os
os.system("cls")

mes = int (input("Ingrese un número de mes: "))

if mes==1 or mes ==3 or mes ==5 or mes==7 or mes==8 or mes ==10 or mes==12:
    print("El mes es de 31 dias")
else:
    print ("No es un mes de 31 días")