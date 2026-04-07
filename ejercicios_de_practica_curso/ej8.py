numeros = [1, 2, 3, 4, 5, 6, 7, 8]
numero_encuentra = int(input("Ingrese que numero quiere encontrar en la lista: "))

for numero in numeros:
    if numero == numero_encuentra:
        print(f"Encontro el numero {numero_encuentra} que indico el usuario ")
    else:
        print(f"No se encontro el numero {numero_encuentra} que indico el usuario")
        break