import os
os.system("cls")

dia = int (input("Ingrese un número de día 1-7: "))

if dia >=1 and dia <=7:
    #dia válido
    if dia == 1: print("Lunes")
    if dia == 2: print("Martes")
    if dia == 3: print("Miércoles")
    if dia == 4: print("Jueves")
    if dia == 5: print("Viernes")
    if dia == 6: print("Sabado")
    if dia == 7: print("Domingo")
else:
    print ("Error, Ingrese valor entre 1 y 7")