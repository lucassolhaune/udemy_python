#Parametros y funciones
from inspect import walktree

#Forma estandar
def saludar (nombre, edad):
    print(f"Hola, m nombre es {nombre} y mi edad es {edad}")

saludar("Lucas", 25)


#Parametros predefinidos
def saludar (nombre, ciudad="Madrid"):
    print(f"Hola, mi nombre es {nombre} y mi ciudad es {ciudad}")

saludar("Lucas", "Buenos Aires" )


#Parametros indefinidos, antes del parametros se escribe un "*"
def dispositivos_electronicos (*dispositivos):
    print("Mis dispositivos favoritos son: ", dispositivos)

dispositivos_electronicos("celular", "tablet", "notebook") #Una especia de tupla


#Parametros arbitrarios, se utiliza un "**" antes del nombre
def perfil_datos_usuario (**datos):
    print("Perfil del usuario: ", datos)

perfil_datos_usuario(nombre="Lucas", edad=25, pais="Argentina") #Diccionario, tipo de estructura (key, value)
