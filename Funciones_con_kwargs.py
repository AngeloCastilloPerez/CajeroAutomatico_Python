'''La sintaxis especial **kwargs en las definiciones de funciones en Python se utiliza para pasar una lista de
 argumentos de longitud variable con palabras clave. Usamos el nombre kwargs con el doble asterisco.
La razón es que el doble asterisco nos permite pasar argumentos de palabras clave (y cualquier cantidad de ellos)'''
# Un ejemplo de cómo usar **kwargs sería en una función que toma un número variable de argumentos con nombre.
# Dentro de la función, puedes acceder a los argumentos con nombre como un diccionario normal

def prueba(num1,num2,*args,**kwargs):

    print(f'el primer valor es {num1}')
    print(f'el segundo valor es{num2}')

    for arg in args:
        print(f"arg = {arg}")

    for clave,valor in kwargs.items():
        print(f"{clave} = {valor}")

args = [100,200,300,400]
kwargs = {'x':'uno','y':'dos','z':'tres'}

prueba(15,50, *args, **kwargs)

'''SALIDA: el primer valor es 15
           el segundo valor es50
           arg = 100
           arg = 200
           arg = 300
           arg = 400
           x = uno
           y = dos
           z = tres
'''