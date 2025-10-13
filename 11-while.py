####                            while                                           ###

contador = 0
while contador < 5:
    print(f"Contador: {contador} ")
    contador += 1 #Actualizando el contador +1
# tener cuidado con los bucles infinitos

print("################# while ######################")

contador = 0
while contador < 5:
    contador += 1

    if contador == 3:
        continue
    print(f"Contador: {contador}")

print("################### Break ####################")

contador = 0
while contador < 5:
    contador += 1

    if contador == 3:
        break
    print(f"Contador: {contador}")