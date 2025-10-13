def obtener_notas() :
    # Funcion para obtener  las notas del usuario
    notas = []
    for i in range (3):
        nota = float(input('Ingrese la nota de la asignatura: '))
        notas.append(nota)
    return notas

def calcular_promedio(notas):
    #Funcion para calcular el promedio de las notas
    return sum(notas) / len(notas)

def determinar_situacion_acedemica(promedio):
    #Fucion para determinar la situacion del estudiante
    if promedio >= 6:
        return 'Aprobado'
    else:
        return 'Reprobado'

print('Bienvenido a la evaluacion estudiantil')
notas_estudiante = obtener_notas()
promeido_estudiante = calcular_promedio(notas_estudiante)

print(f'Tu promedio es: {promeido_estudiante: .2f}. Estas {determinar_situacion_acedemica(promeido_estudiante)}')