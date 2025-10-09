## if, elif, else

##Determinar si un numero es par.
num = int(input("Ingrese el numero por favor: "))

if(num % 2 == 0): # Si el resto de la division me da 0 es PAR, sino NO.
    print("El numero es par")
else:
    print("El numero es impar")


##Validar el signo de un numero
x = int(input("Ingrese el un numero: "))

if x > 0:
    print("EL numero es positivo")
elif x == 0:
    print("El numero es cero")
else:
    print("El numero es negativo")

