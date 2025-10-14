#Alcence (Scope) y Espacios de Nombres(Namespaces)
#Ejemplo de alcance y espacios de nombre

x = 'global x' #variable global

def outer():
    x = 'outer x' # variable en alcance que encierra (enclosing)

    def inner():
        nonlocal x # Se refiere a la x del outer
        x = 'inner x' # variable local de inner
        print('Inner: ', x)

        inner()
        print("Outer: ", x)

outer()
print('Global: ', x)