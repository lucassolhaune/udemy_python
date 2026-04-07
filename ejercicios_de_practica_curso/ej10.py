paises_capitales = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
    "Estados Unidos": "Washington",
    "España": "Madrid",
    "Canada": "Ottawa",
    "Noruega": "Oslo"
}

print("Países disponibles:")
for pais in paises_capitales:
    print(pais)

pais_encontrar = input("Ingrese un país de la lista: ")

if pais_encontrar in paises_capitales:
    capital = paises_capitales[pais_encontrar]
    print(f"La capital de {pais_encontrar} es {capital}")
else:
    print("El país no se encuentra en el diccionario")