##Operadores logicos

#and, or, not

#and
edad = 25
tiene_experiencia = True

if edad > 18 and tiene_experiencia: #Ambas tienen que ser verdaderas, de lo contrario es Falso.
    print("Esta contradado!!!")
else:
    print("No cumple los requisitos")

#or
es_estudiante = True
es_trabajador = False

if es_estudiante or es_trabajador: #Es verdadero si al menos una de ella cumple.
    print("La persona es estudainte o empleado")
else:
    print("La persona no es estudiante ni empleado")

#not
llueve = False

if not llueve:
    print("No esta lloviendo")
else:
    print("Esta lloviendo")


