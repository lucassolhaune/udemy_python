conjunto_vacio = set()
numeros = {1, 2, 3, 4, 5}
frutas = {'manzana', 'banana', 'cereza'}

for fruta in frutas:
    print(fruta)

print('-------------------------------------------------------')

#No existe un orden porque no es una estructura ordenada. Por eso no se pueden acceder a su posicion
#La unica forma es grupal
frutas = {'manzana', 'banana', 'cereza', 'manzana'}
for fruta in frutas:
    print(fruta)

#agregamos un mango en el conjunto de frutas
frutas.add("mango")
for fruta in frutas:
    print(fruta)

#Eliminamos mango del conjunto de frutas
frutas.remove("mango")

print("-----------------------------------------------")
#Eliminamos el numero 3 del conjuntos de numeros
print(numeros)
numeros.discard(3)
print(numeros)

#Agregamos los numeros "7,8,9,10" al conjunto de numeros
numeros.update([7,8,9,10])
print(numeros)

#False, pregunto si 20 esta en el cinjunto numeros
print(20 in numeros)

print("-----------------------------------------------")

##### Unir conjuntos #####
a = {1,2,3,4}
b = {3,4,5,6}
print(a | b) #{1, 2, 3, 4, 5, 6, 7, 8}
print(a & b) #Me devuelve {3, 4} que son los numeros que se comparten los "dos sets"
print(a - b) #Me devuelve {1, 2} que son los dos numeros que no tiene el conjunto "b"
print(b - a) #Me devuelve {5, 6} que son los dos numeros que no tiene el conjunto "a"
print(a ^ b) #Me devuelve {1, 2, 5, 6} que son todos los numeros que no estan en la interseccion de los conjuntos


"""
Transformamos una lista en un conjunto para eliminar elementos repetidos para luego volver
a trasnformalo en una lista.
"""
#Lista
ids = [2,3,1,3,4,5]
print(ids) # [2,3,1,3,4,5]

#Conjunto
ids = set(ids) #De esta forma elimino los numeros repetidos
print(ids) # [1, 2, 3, 4, 5]

#Lista
ids = list(ids) # [1, 2, 3, 4, 5]
print(ids)
    

