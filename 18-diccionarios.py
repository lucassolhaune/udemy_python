#Los Diccionarios son mutables

diccionario_vacio = {}

#Diccionario persona con datos
persona = { "nombre": "Juan", "edad": 30, "ciudad": "Madrid" }
print(persona)

#Me devuelve la  edad de la persona
print (persona.get('edad')) #30

#valor no encontrado porque apellido no exite.
print(persona.get('apellido', 'valor no encontrado')) 

#Modifico el valor de la clave. 30 a 35
persona["edad"] = 35
print(persona)

#Añadir la profesion clave valor
persona['profesion'] = 'Ingeniero'
print(persona) # Se agrega al final del diccionario la profesion

#Borrar elemento, no aparecera ciudad dentro del diccionario
del persona ["ciudad"]
print(persona)

#borrar con .pop(). Nos devuelve el elemento 'Ingeniero' que es lo que borramos
profesion = persona.pop('profesion')
print(profesion) #Ingeniero


#Operaciones basicas
claves = persona.keys()
print(claves) #dict_keys(['nombre', 'edad'])

valores = persona.values()
print(valores) #dict_values(['Juan', 35])

elementos = persona.items()
print(elementos)  #dict_items([('nombre', 'Juan'), ('edad', 35)]) tupla: key, value

#Longitud del diccionario
print (len(persona)) #2 elementos

#Iterar sobre las claves:
for clave in persona:
    print(clave) #nombre edad

#Iterar sobre los valores:
for valor in persona.values():
    print(valor) #Juan 35

#Iterar sobre clave, valor
for clave, vlaor in persona.items():
    print(clave, valor) #nombre: 35,  edad: 35
