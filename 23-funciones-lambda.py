## Funciones Lambda --> Funciones anonimas
#lambda argument: expression -> DEFINICION

suma = lambda  a,b : a + b
print(suma(5,6)) #11

print("====================CUADRADOS DE CADA NUMERO=========================")

##map(), filter(), sorted()
# numeros = [1, 2, 3, 4, 5]
# cuadrado = [n ** 2 for n in numeros] ##Me devuelva el cuadrado de cada numero. Numero por numero.
# print(cuadrado)

numeros = [1, 2, 3, 4, 5]
cuadrados = list(map(lambda x: x**2, numeros)) # ("x"-> argumento), ("x**2" -> expresion que devuelve), "numeros" -> lista que recibe la funcion
print(cuadrados) # [1, 4, 9, 16, 25

print("===================PARES==========================")

numeros = [1, 2, 3, 4, 5, 6]
pares = list(filter(lambda x: x%2 == 0, numeros))
print(pares) # 2, 4, 6


print("=====================ORDENAR ELEMENTOS DE UNA LISTA SEGUN UN CRITERIO DEFINIDO========================")

dispositivos = ['celular', 'auriculares','tablet', 'televisor']
dispositivos_ordenados = sorted(dispositivos, key=lambda dispositivo: len(dispositivo)) # Me devuelve los numeros del menor caracter al que mas tiene
print(dispositivos_ordenados)

