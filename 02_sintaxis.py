#Consideraciones Importantes y sintaxis

#Funcion con bucle for y condicional if-else
def imprimir_numeros_pares_hasta_n(n):
    """
    Imprime todos los numeros pares desde 0 hasta el numero n (incluido).
    """
    for i in range(n + 1):
        if i % 2 == 0: #Verifica si el numero es par
            print(f"{i}, (PAR) ")
        else:
            print(f"{i}, (IMPAR)")

#Uso de la funcion
limite = 100
print(f"Numeros pares hasta (limite): ")
imprimir_numeros_pares_hasta_n(limite)
