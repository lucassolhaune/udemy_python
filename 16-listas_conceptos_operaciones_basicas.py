l1 = [2, 3, 4]

frutas = ["manzanas", 3, "banana"]

print(frutas[0])
print(frutas[1])

#modifico el elemento en la posicion 1
frutas[1] = "pera"
print(frutas)

#.append agrega un elemento al final de la lista
frutas.append("naranja")
print(frutas)

#inserto kiwi en la posicion 1
frutas.insert(1, "kiwi")
print(frutas)

#elimino kiwi de la lista
frutas.remove("kiwi")
print(frutas)

#elimino la posicion 1
del frutas[1]
print(frutas)

# elimina el elemento pero devuelve un resultado que lo guardamos en la variable ultimo
ultimo = frutas.pop()
print(ultimo) #naranja

#longitud de la lista "len"
print(len(frutas))

#recorro la lista frutas
for fruta in frutas:
    print(fruta) # manzana, banana

#transformalo a lista
palabra = "Hola"
caracteres = list(palabra)
print(caracteres) # ['H', 'o', 'l', 'a']
