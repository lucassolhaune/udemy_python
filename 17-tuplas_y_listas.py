#Tuplas inmutables

colores = ("rojo", "verde", "azul")
print(colores)

#va a quedar siempre vacia porque no se puede modificar
tupla_vacia = ()

#puedo agregarle valores o modificarla
lista_vacia = []

#tupla de un solo elemento
solo_una = (5,)
print(solo_una)

print(colores[0]) # rojo
print(colores[-1]) # azul

lista_colores = ["rojo", "verde", "azul"]
lista_colores[0] = "negro"
print(lista_colores) # ['negro', 'verde', 'azul']

t1 = (1, 2, 3)
t2 = (4, 5, 6)

t3 = t1 + t2

print(t3) # (1, 2, 3, 4, 5, 6) concatena o suma la tupla

print(3 * t1) # (1, 2, 3, 1, 2, 3, 1, 2, 3) me multiplica la tupla por 3

print(7 in t1) # corrobora si 7 esta en la tupla ---> False

print ("#######################")

for color in colores:
    print(color) # rojo, verde, azul
    
print ("#######################")

print (t1 [1:3]) # (2, 3) te da un 