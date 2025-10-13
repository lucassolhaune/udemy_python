#Funciones con multiples parametros
def suma (a, b):
    return print(a + b)

suma(3, 5)

print("==========================================================================")

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    producto = a * b
    division = a / b
    return print({'suma':suma,'resta': resta, 'producto': producto, 'division': division}) #diccionario

operaciones_basicas(16,4)

print("==========================================================================")

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    producto = a * b
    division = a / b
    return print(suma, resta,  producto, division)

n,m = 10,7 #    
print (operaciones_basicas(n,m))