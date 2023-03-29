#Un método es una función que “pertenece a” un objeto. En Python, el término método no está limitado a instancias de clase: otros tipos de objetos pueden tener métodos también. Por ejemplo, los objetos lista tienen métodos llamados append, insert, remove, sort, y así sucesivamente.
#Hay tres tipos de métodos en Python: métodos de instancia, métodos de clase y métodos estáticos.
#Aquí emplearemos solo los metodos de isntancia

#Recuerda:Para crear clase usar>> class .... :
class Pajaro:

    def __init__(self,color, especie):
        self.color = color
        self.especie = especie
#Tambien se pueden crear metodos : def METODO(self) /siempre debe ir self!
    def piar(self):
        print('pio, mi color es {}'.format(self.color))
    def volar(self,metros):
        print(f"El pajaro ha volado {metros} metros")
piolin = Pajaro('amarillo','canario')
#Al llamar piar se ejecuta "print('pio, mi color es {}'.format(self.color))" asignado en el metodo piar-(line8)
piolin.piar()
piolin.volar(3) # se le debe asignar los metros ya que son un valor asignado en el metodo volar


