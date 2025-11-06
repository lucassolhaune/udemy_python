import csv
import json
from PIL import Image

with open('datos.csv', mode= 'w') as archivo:
    escritor = csv. writer(archivo)
    escritor.writerow(['NOMBRE', 'EDAD', 'CIUDAD'])
    escritor.writerow(['Lucas', '25', 'Argentina'])
    escritor.writerow(['Juan', '10', 'Nueva York'])
    escritor.writerow(['Angel', '35', 'Bolivia'])

#Lee los datos, me los muestra en forma de tabla
with open('datos.csv', mode='r') as archivo:
    lector = csv.reader(archivo)
    for fila in lector:
        print(fila)

#Crea un archivos json con datos
with open('datos.json', 'w') as archivo:
    json.dump({'nombre': 'Lucas', 'edad': 25}, archivo)

with open('datos.json', 'r') as archivo:
    datos = json.load(archivo)
    print("json:", datos)

#Abrir imagen
imagen = Image.open('martillo.jpg')
imagen.show()

#Convertir imagen a escalas de grises
imagen_gris = imagen.convert('L')

#Guardar la imagen nueva gris
imagen_gris.save('martillo_gris.jpg')