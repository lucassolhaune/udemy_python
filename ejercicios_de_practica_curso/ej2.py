# Número mayor
# Pedile dos números al usuario e imprimí cuál es mayor (o si son iguales).

n1 = int(input("Ingrese un numero: "))
n2 = int(input("Ingrese un numero: "))

if n1 > n2:
    print("El primer numero ingresado es mayor al segundo")
elif n2 > n1:
    print("El segundo numero ingresado es mayor al primero")
else:
    print("Los dos numeros ingresados son iguales")