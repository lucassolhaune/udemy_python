# for, break, continue

secuencia = [1,4,5,6,7]
for elemento in secuencia:
    if elemento == 5:
        #break --> mata el bucle dada una condicion
        continue # --> saltarse un paso y no ejecutar el codigo pero si los siguientes pasos de la iteracion del bucle dada una condicion
    print(elemento)


print("#################################")
for letra in "Python":
    print(letra)


print("#################################")
lista = [1,4,5,6,7]
for i in range(len(lista)):
    print(lista[i])


print("#################################")
for i, value in enumerate(lista):
    print(f"Elemento {i}: {value}") #Formateo de cadenas de texto "i = llave", "value = valor"

