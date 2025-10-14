from multiprocessing.managers import ValueProxy

#Estructura basica de una clase
import valor

class NombreDeLaClase:
    #Atributo de la clase
    atriburo_de_clase = valor

    def __init__(self, parametro1, parametro2): #metodo constructor
        #Atributos de instancia
        self.parametro1 = parametro1
        self.parametro2 = parametro2

    #Metodo de instancia
    def metodo_de_instancia(self):
        #Codigo del metodo
        return self.parametro1 + self.parametro2


class DataSet:
    tipo_Dato = 'numerico'
    def __inti__ (self, data):
        self.data = data

    def media(self):
        '''Devuelve la media de los datos.'''
        return sum(self.data) / len(self.data)