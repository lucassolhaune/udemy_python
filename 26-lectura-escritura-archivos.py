archivo = open('prueba.txt', 'r')
contenido = archivo.read()
print(contenido)

archivo = open('pueba.txt', 'w') 
archivo.write('Hola, mundo!\n')
archivo.close()


with open('prueba.txt', 'r') as archivo: # 'R' -> Modo lectura
    contenido = archivo.read()

with open('prueba.txt', 'w') as archivo: # 'W' -> Sobrescribe el archivo
    archivo.write('Adios')

