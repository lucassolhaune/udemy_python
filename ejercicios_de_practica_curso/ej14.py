numeros = [4, 7, 1, 45, 23, 89, 2, 10, 3]

max_num = numeros[0]
min_num = numeros[0]

# Iterar sobre la lista de números para encontrar el número mayor y menor
for num in numeros:
    if num > max_num:
        max_num = num
    if num < min_num:
        min_num = num

# Imprimir los numeros mayores y menores que contiene el array
print(f"El numero mayor del array es: {max_num}")
print(f"El numero menor del array es: {min_num}")