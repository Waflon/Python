import os
os.system("cls")

ciclo = True
print ("ciclo es de tipo ", type(ciclo))

while True:
    respuesta = input("desea salir del ciclo s/n")
    if respuesta == "s":
        break
    print("íltima línea del ciclo while")
print ("fin del ciclo while")