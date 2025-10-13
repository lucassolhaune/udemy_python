###Funciones
#Funcion con return
def mi_funcion(param1, param2):
    resultado = param1 + param2
    return resultado

print (mi_funcion(3, 5)) # 8

###########################################
#Funcion sin return
def saludar (nombre, saludo):
    print(f"{saludo}, {nombre}!!")

saludar ("Hola", "Lucas") # Hola, Lucas!! 

###########################################
def cuadrado(x):
    return x ** 2

resultado = cuadrado(5)
print(resultado)

resultado = cuadrado(8)
print(resultado)

###########################################
def imprimir_mensaje():
    print("Hola mundo")

resultado = imprimir_mensaje() # HoLA MUNDO


###########################################

x = 10 
def mi_funcion():
    y = 5
    print("Esta funcion imprime el numero: ", x + y)

mi_funcion() # Imprime x = 10, y = 5

############################################

