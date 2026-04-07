numero_de_dia = int(input("Ingrese un numero de dia(1 a 7): "))

while numero_de_dia >= 1 or numero_de_dia <= 7:
    match numero_de_dia:
        case 1: 
            print("Lunes")
            break
        case 2:
            print("Martes")
            break
        case 3:
            print("Miercoles")
            break
        case 4:
            print("Jueves")
            break
        case 5:
            print("Viernes")
            break
        case 6:
            print("Sabado")
            break
        case 7:
            print("Domingo")
            break
        case default:
            print("Ingrese un numero valido")
            break