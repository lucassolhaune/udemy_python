##FUNCIONES##

#Ejemplo sin funciones
#Dimensiones del rectangulo 1
base1 = 5
altura1 = 10
area1 = base1 *altura1
print("Area del rectangulo 1 es: ", area1)

#Dimensiones del rectangulo 2
base2 = 7
altura2 = 10
area2 = base2 * altura2
print("Area del rectangulo 2 es: ", area2)

#Dimensiones del rectangulo 3
base3 = 9
altura3 = 4
area3 = base3 * altura3
print("Area del rectangulo 3: ", area3)

#Ejemplo con funciones
def calcular_area_rectangulo(base, altura):
    """Calcula el area de un rectangulo"""
    return print("El area calculada es: ", base * altura)

calcular_area_rectangulo(3,5)
calcular_area_rectangulo(2,10)
calcular_area_rectangulo(10,9)