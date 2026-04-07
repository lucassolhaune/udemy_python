numeros = [1, 2, 3, 54, 34, 90, 86, 6, 10, 12]

numeros_pares = []

for num in numeros:
    if num % 2 == 0:
        # Si los numeros del array son disibles por cero 
        numeros_pares.append(num) 

print(f"Los numeros pares son: {numeros_pares} ")