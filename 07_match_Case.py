#Match, case es similar al switch --> NO se usa casi nunca

# numero = int(input("Ingrese una opcion del (1 al 3): "))

# match numero: 
#     case 1:
#         print("Opcion vegetariana")
#     case 2:
#         print("Opcion normal")
#     case _:
#         print("Ningua opcion")

# ###############################

# numero = int(input("Ingrese un numero: "))

# match numero:
#     case 0:
#         print("cero")
#     case n if n > 0: #n es una variable local. Si n es mayor a cero, entonces es positivo.
#         print("Positivo")
#     case n if n < 0:
#         print("Negativo")
#     case _:
#         print("No se puede clasificar")
            
###########################
imc = float(input("Ingrese su IMC (indice de masa coroporal): "))

match imc:
    case valor if 0 < valor <= 18.5:
        print("Bajo peso")
    case valor if 18.5 < valor <= 24.9:
        print("Peso normal (saludable)")
    case valor if 24.9 < valor <= 29.9:
        print("Sorepeso")
    case valor if 29.9 < valor <= 34.9:
        print("Obesidad clase 1 (moderada)")
    case valor if 34.9 < valor <= 39.9:
        print("Obesidad clase 2 (severa)")
    case valor if 39.9 <= valor :
        print("Obesidad clase 3 (muy severo)")
    case _:
        print("Valores de IMC no validos")