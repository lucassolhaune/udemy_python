def evaluar_expresion(expr):
    componentes = expr.split()

    match componentes:
        case [a, "+", b]:
            return int(a) + int(b)
        case [a, "-", b]:
            return int(a) - int(b)
        case [a, "*", b]:
            return int(a) * int(b)
        case [a, "/", b]:
            if int(b) == 0:
                return "Error: División por cero"
            return int(a) / int(b)
        case _:
            return "Expresión no válida"

expresion = "5 * 3"
resultado = evaluar_expresion(expresion)

print(f"El resultado de '{expresion}' es: {resultado}")