import os
os.system("cls")

contadorMayores=0
contadorMenores=0
for i in range(10):
    edad= int(input(f"Ingrese Edad numero {i+1}: "))
    if(edad>=18):
        contadorMayores = contadorMayores + 1
    if(edad<18):
        contadorMenores = contadorMenores + 1
    os.system("cls")
    
print("El total de mayores de edad es: ", contadorMayores)
print("El total de menores de edad es: ", contadorMenores)
