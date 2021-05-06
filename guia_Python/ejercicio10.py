import os
os.system("cls")

sueldo = int(input("Ingrese su sueldo: "))

if sueldo >=1 and sueldo <= 250000:
    print("su bono es de $150.000-")
elif sueldo >250000 and sueldo <= 500000:
    print("su bono es de $100.000-")
elif sueldo >500000 and sueldo <= 850000:
    print("su bono es de $50.000-")   
else:
    print("Fuera de rango-")  