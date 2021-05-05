import os
os.system("cls")

ciclo = True
print ("ciclo es de tipo ", type(ciclo))

while ciclo:
    respuesta = input("desea salir del ciclo s/n")
    if respuesta == "s":
        ciclo = False
    print("íltima línea del ciclo while")
print ("fin del ciclo while")