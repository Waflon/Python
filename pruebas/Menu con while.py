import os
import msvcrt
os.system("cls")

#inicializar variables
a = 0
b = 0
resultado = 0
opcion = 0
while True:
    os.system("cls")
    print("    Menú     ")
    print("-------------")
    print("")
    print("1 Sumar")
    print("2 Restar")
    print("3 Salir\n")  #\n salto de línea  
    print(" ")
    opcion = int(input("Ingres una opción [1-3]:"))

    if opcion == 1:
        os.system("cls")
        print("    Sumar    ")
        print("-------------")
        print("")   
        a = int(input("Ingrese un valor para a "))
        b = int(input("Ingrese un valor para b "))
        resultado = a + b
        print("La suma es ", resultado)

    if opcion == 2:
        os.system("cls")
        print("    Restar    ")
        print("-------------")
        print("")   
        a = int(input("Ingrese un valor para a "))
        b = int(input("Ingrese un valor para b "))
        resultado = a - b
        print("La resta es ", resultado)

    if opcion == 3:    
        break
    #hacer una pausa
    print("Presionte tecla para continuar")
    msvcrt.getch()
    #os.system("pause")
    #input("Presionte Enter para continuar...")
print("fin del menú")    