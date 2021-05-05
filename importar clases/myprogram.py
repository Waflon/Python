import os
os.system("cls")
from funcionesTarea import Tarea


print("Menu principal")
print("para sumar, presione 1")
print("para restar, presione 2")
print("para salir, presione cualquier otro valor")
opcion = int(input())

os.system("cls")

while((opcion<3) and (opcion>0)):  
    x=int(input("Ingrese un valor para x: "))
    y=int(input("Ingrese un valor para y: "))
    tarea = Tarea(x,y)

    if (opcion==1):
        tarea.suma()
    if (opcion==2):
        tarea.resta()
    os.system("pause")
    os.system("cls")
    print("Menu principal")
    print("para sumar, presione 1")
    print("para restar, presione 2")
    print("para salir, presione cualquier otro valor")
    opcion = int(input())

        