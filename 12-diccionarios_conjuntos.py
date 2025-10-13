#Objeto mutable

mi_diccionario = {"clave1": 3, "clave2": 5, "clave3": 7} # llave - valor
valor = mi_diccionario["clave1"]
print(valor) # 3 porque traigo el valor de clave

mi_diccionario["clave1"] = 10
print(mi_diccionario) # modifique clave1

mi_diccionario["clave4"] = 10
print(mi_diccionario) # se agrego al final del diccionario

mi_diccionario.pop("clave3")
print(mi_diccionario) # borra la clave3

#Forma de iterar en diccionarios
#De esta forma tendriamos "llave-valor"
for clave, valor in mi_diccionario.items():
    print(f"clave: {clave}, valor: {valor}")
"""
"clave1":valor1, 
"clave2":valor2, 
"clave3":valor3
"""

for elemento in mi_diccionario:
    print(elemento)
"""
clave1
clave2
clave4
"""
print("####################################")
#De esta forma tendriamos las keys
print(mi_diccionario.keys())

#De esta forma tendriamos los valores
print(mi_diccionario.values())

#De esta me devuelve una lista de tuplas --> "llave-valor"
print(mi_diccionario.items()) 

print("####################################")

##COnjuntos
mi_set = {1, 3 ,9} #Elementos
print(mi_set)

set1 = {1, 2, 3}
set2 = {3, 4, 5}
print (set1 | set2) # une los set {1, 2, 3, 4, 5}

print (set1 & set2) # {3}

print(set1 - set2) # todos los elementos que son distintos del set1 = {1, 2}
print(set2 - set1) # todos los elementos que son distintos del set2 = {4, 5}

print(len(set1)) # 3

print(len(mi_diccionario)) # 3

print (4 in set1) #False. 4 se encuentra en set1?
###
mi_set = {1, 3, 9, 3}
print(mi_set)
mi_set.add(20) # Agrego el 20 a mi_Set
print(mi_set) # Se muestra mi_set con el 20 agregado

mi_set.remove(3)
print(mi_set) # Se muestra mi_set sin el 3

lista = [1, 3, 3, 5, 7, 7]
set(lista) # elimina los elementos repetidos
#[1, 3, 5, 7] quedaria.