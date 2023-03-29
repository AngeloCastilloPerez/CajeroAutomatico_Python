#A continuación mostrare como crear una clase con diferentes tipos de metodo.

class Pajaro:

    alas = True

    def __init__(self,color, especie):
        self.color = color
        self.especie = especie
#Un metodo puede:
    #cambiar otro metodo asignado en la class
    def piar(self):
        print('pio, mi color es {}'.format(self.color))
    #de asginar metodos dentro de otro metodos
    def volar(self,metros):
        print(f"El pajaro ha volado {metros} metros")
        self.piar()
    def pintar_negro(self):
        self.color = 'negro'
        print(f"Ahora el pajaro es {self.color}")

    @classmethod  # metodo de clase
    def poner_huevos(cls,cantidad):
        print(f"Puso{cantidad} huevos")

    @staticmethod
    def mirar():
        print("El pajarito mira")
Pajaro.poner_huevos(4) # se puede ejecutar por que es un methodo de clase, no necesita

#Pajaro.piar() # no se ejecuta porque no tiene instancia(self)
piolin = Pajaro('verde','canario')
# Al llamar volar se obtiene su valor print y el metodo piar agregado
piolin.volar(2) # se le debe asignar un valor por los metros
piolin.mirar()
piolin.pintar_negro()
