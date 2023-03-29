from random import shuffle

#lista inicial
palitos = ['-','--','---','----']

#mezclar palitos
def mezclar(lista):
    shuffle(lista)
    return lista

#pedir intento a jugador
def probar_suerte():
    intento = ''

    while intento not in ['1','2','3','4']:
        intento = input("Elige un numero del 1 al 4: ")
    
    return int(intento)

#comprobar intento
def chequear_intento(lista,intento):
    if lista[intento-1] == '-':
        print("A lavar los platos")
    else:
        print("Esta vez te salvaste por poquito")

    print(f"Te ha tocado{lista[intento-1]}")

#invocamos a las funciones:
palitos_mezclados = mezclar(palitos)
seleccion = probar_suerte()
chequear_intento(palitos_mezclados,seleccion) 

'''SALIDA: Elige un numero del 1 al 4: 3
           Esta vez te salvaste por poquito
           Te ha tocado--'''
