'''Dejame felicitarte por tu interés en seguir aprendiendo!
Te preguntaras que es una función dínamicauna? bien, función dinámica se refiere a una función que se puede crear
 y modificar en tiempo de ejecución. Esto se logra utilizando la función incorporada exec, que permite 
 ejecutar código Python dinámicamente. 
'''
#DEFINIENDO FUNCIÓN DINAMICA

#Primero escribimos la función condicionando el retorno con range(buscamos un valor entre 2 números)
#Para este ejemplo revisamos si el número insertado tiene 3 cifras y guardamos en una variable 

def chequear_3_cifras(numero):
    return numero in range(100,1000)

resultado = chequear_3_cifras(655)
print(resultado)

#Salida: TRUE 

#Para crear la misma función pero que me regrese los número entre 100 y 999 y no solo TRUE o FALSE, debemos ejecutar:


def chequear_3_cifras(lista):

    lista_3_cifras = []

    for n in lista:
        if n in range(100,1000):
            lista_3_cifras.append(n)
        else:
            pass
    return lista_3_cifras

resultado = chequear_3_cifras([965,555,44444,444])
print(resultado)

#Salida: [965,555,444] #Los números que estan entre 100 y 999 de la lista.

#Felicidades, creaste una función dinámica para imprimir la palabra "Hola"/puedes cambiar la palabara Hola por cualquier otra y colocar cálculos aritmeticos también

