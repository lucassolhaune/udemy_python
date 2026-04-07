#Lista por comprension

#[nueva_expresion for elemento in iterable if condicion], me la devuelve ordenada
cuadrados = [x ** 2 for x in range (10) if x % 2 == 0] # x al caudrado para x en el rango de (0 a 10)
print("Lista:" ,cuadrados)

#{nueva_expresion for elemento in iterable if condicion}, no me los devuelve ordenados.
cuadrados_sets = {x ** 2 for x in range(10)}
print("sets:" ,cuadrados_sets)

#{clave: valor for elemento}