'''Hola, soy Angelo Castillo, dejame felicitarte por tu interés en seguir aprendiendo!
Te preguntaras que es una función?, una función es un bloque de código que solamente se ejecuta
cuando es llamada. Puede recibir información (en forma de
parámetros), y devolver datos una vez procesados como
resultado.
'''
#DEFINIENDO FUNCIÓN SIN RETURN

#Primero escribimos DEF(palabra clave para definir fucniones)/como tip para no olvidar, siempre "DEF"inimos la función!
#Continuamo definiendo el nombre de la función, en este caso "First_function"(SIEMPRE COLOCAR ":" AL FINAL)
#agregamos la acción que deseamos ejecutar, en este caso -print("Hola")

def First_function():
    print("Hola")
#Para llamar a la función, solo debemos utilizar el nombre asignado
First_function()

#Salida: Hola
#Felicidades, creaste una función para imprimir la palabra "Hola"/puedes cambiar la palabara Hola por cualquier otra ycolocar cálculos aritmeticos también 

#Luego según la necesidad de nuestro proyecto podemos agregar el argumento que contiene información que se tranforma en un resultado
#Ejemplo:

def Second_function(name): #name es argumento que ingresamos para este caso
    print("Hola " + name)

#Esta vez, ya que ingresamos un argumento al definir nuestra función, debemos llamarla junto al argumento que deseamos ingresar, no llamar a la función sin algún argumento, genera un error
Second_function("Campeon")

#OUT : Hola Campeon

#Felicidades, creaste una función para imprimir tu función agregando un argumento "name", sigue aprendiendo, eres un exito!

#DEFINIENDO FUNCIÓN CON RETURN
#Para que una función pueda devolver un valor (y que pueda ser almacenado en una variable, por ejemplo), utilizamos la declaración return .
#En el siguiente ejemplo, creamos una función que multiplica 2 numeros,
def Return_function(number1,number2):
    return number1*number2
#Debemos insertar en una variable para poder vizualizar el resultado, agregando los números de su elección
nueva_variable = Return_function(6,7)
print(nueva_variable)

#OUT : 42

