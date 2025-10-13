#Listas y tuplas
mi_lista = [1, 2, 3, "Hola", True]
mi_tupla = [1, 2, 3, "Hola", True]

print(mi_lista[2]) # 3
print(mi_tupla[3]) # "Hola"

"""
La diferencia entre la lista y tupla es que la tupla es inmutable, no se le puede cambiar 
los valores que tiene dentro, en cambio la lista si, yo puedo reasignarle otro valor. 
"""

mi_lista.append(8)
print(mi_lista) # Agrego un 8 en la ultima posicion

print(len(mi_lista)) # 6
print(len(mi_tupla)) # 5

mi_lista.remove(3)
print(mi_lista)

############################

lista1 = ['a','b','c']
lista2 = lista1
lista2[1] = 'z'
print(lista2)

lista3 = lista1.copy()
lista3 = 'd'
print(lista3)

##################### Join ---> Une las letras ######################  Split --> las separa
letras ='-'.join(lista1)
print(letras)