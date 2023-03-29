#Supongamos que deseas agregar un número ilimitado de argumentos
#Si usas *args(podrias reemplazar args por cualquier otra palabra)
#te permitira agregar un numero ilimitado de datos, ejemplo:

def suma(*args):
    total = 0

    for arg in args:
        total += arg
    return total

print(suma(5,6,8))

#SALIDA : 19

#Forma resumida:

def suma(*args):

    return sum(args)

print(suma(5,6,8))

#SALIDA : 19

#Te recomiendo usar ARGS, con ello trabajamos de forma respetuosa hacia otros desarrolladores de codigo
