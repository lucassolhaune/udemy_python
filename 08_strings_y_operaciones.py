#Cadenas de texto y operaciones con strings

palabra0 = "Fargo"
print(palabra0) # Fargo
print(palabra0[0]) # F

palabra1 = "Lucas"
print(palabra1)

palabra2 = palabra0 + palabra1
print(palabra2) # FargoLucas
print(palabra2[0:4]) #Farg -> porque va desde la primer posicion hasta la cuarta, o puede ir desde otra posicion

print(len(palabra0)) # 5

print(palabra0[-1]) # o -> ultima letra de la palabra Fargo

print (palabra0.upper()) #FARGO
print (palabra0.lower()) #fargo

palabra3 = "jorge".capitalize() # La "j" se pondra solamente en mayuscula con el metodo capitalize()

#.split() convierte la variable en una lista.

