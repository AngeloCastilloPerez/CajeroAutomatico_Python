
#Las clases de definen con la palabra clave : CLASS
#Recordar que es comun dejar la primera letra de la clase en mayuscula, ejemplo: Producto

#Podemos pensar a las clases como el "plano" o "plantilla" a partir del cual podemos crear objetos individuales, con propiedades y métodos asociados

class Perro:
    pass

mi_perro = Perro()
otro_perro =Perro()

print(type(mi_perro))
print(type(otro_perro))

'''SALIDA: <class '__main__.Perro'>
            <class '__main__.Perro'> '''
#Al incluir en una variable la clase, el tipo sigue siendo una clase en ambas

#Ejemplo 2, crearemos un atributo COLOR  para la clase PERRO:

class Perro:
    
    def __init__(self, color):
        self.color = color
       

mi_perro = Perro('blanco')

print(mi_perro.color)

#Salida : Blanco


#Que pasa si deseas agregar parametros y atributos? :

class Perro:

    def __init__(self, color, peso, edad, raza):
    
        self.color = color
        self.peso = peso
        self.edad = edad
        self.raza = raza


mi_perro = Perro('blanco',24,15,'siberiano')


print(mi_perro.color)
print(mi_perro.peso)
print(mi_perro.edad)
print(mi_perro.raza)
'''Salida : blanco
           24
           15
           siberiano'''
