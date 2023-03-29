# CajeroAutomatico_Python

##Es necesario que sepas como crear funciones y otras cosas para poder avanzar y entender este proyecto.Revisar archivos adjuntos:

1.Crear una función
2.Crear Función Dinámica
3.Funciones con tuplas
4.Funciones con ARG
5.Funciones con KWARGS
6.Juego de palitos(practica funciones)
7.Crear una clase
8. Que son los métodos?
9. Tipos de métodos


##Proyecto Cajero Automático:

###Este proyecto es sencillo, buscamos crear un registro de un Cliente en nuestro banco, el podría retirar o depositar dinero, dependiendo de su saldo

'''Este código define una clase Cliente, que es una subclase de la clase Persona. 
La clase Cliente tiene cuatro funciones: __init__, __str__, depositar y retirar. 
La función __init__ inicializa las variables de instancia nombre, apellido,
 numero_cuenta y balance. La función __str__ devuelve una cadena de texto 
 que representa al objeto Cliente. Las funciones depositar y retirar 
 realizan transacciones bancarias.'''

#Crear clase Persona
class Persona:
    #Definir __init__ agregando Nombre y apellido
    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido
#Crear clase Cliente()
class Cliente(Persona):
    #Definir __init__ agregando nombre,apellido,numero de cuenta y balance
    def __init__(self, nombre,apellido,numero_cuenta,balance = 0):
        super().__init__(nombre,apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        return f"Cliente: {self.nombre}{self.apellido}\nBalance de cuenta {self.numero_cuenta} : ${self.balance}"

    def depositar(self,monto_deposito):
        self.balance += monto_deposito
        print("Deposito aceptado")

    def retirar(self,monto_retiro):
        if self.balance >= monto_retiro:
            self.balance -= monto_retiro
            print("Retiro realizado")
        else:
            print("Fondos insuficientes")


'''La función crear_cliente solicita información al usuario, crea una instancia de la clase Cliente y devuelve la instancia. 
La función inicio llama a la función crear_cliente y luego ejecuta un ciclo de repetición en el que se solicita al usuario 
que seleccione una operación (depositar, retirar o salir). Dependiendo de la opción seleccionada, se llama a las funciones
 depositar o retirar en la instancia de Cliente, y se muestra el saldo actualizado. El ciclo de repetición se repite hasta 
 que se seleccione la opción "S" para salir.'''
#Definir función crear_cliente()
def crear_cliente():
    nombre_cl = input("Ingrese su nombre: ")
    apellido_cl = input("ingrese su apellido: ")
    numero_cuenta = input("Ingrese su numero de cuenta: ")
    cliente = Cliente(nombre_cl,apellido_cl,numero_cuenta)
    return cliente
#Definir función inicio()
def inicio():
    mi_cliente = crear_cliente()
    print(mi_cliente)
    opcion = 0

    while opcion != 'S':
        print('Elije: Depositar (D), Retirar (R), o Salir(S)')
        opcion = input()

        if opcion == 'D':
            monto_dep = int(input("Monto a depositar: "))
            mi_cliente.depositar(monto_dep)
        elif opcion == 'R':
            monto_ret = int(input("Monto  a retirar: "))
            mi_cliente.retirar(monto_ret)
        print(mi_cliente)

    print("Gracias por operar en el banco de Angelo Castillo")

inicio()

<a href="https://www.instagram.com/angelocastilloperz/">
  <img align="left" alt="Abhishek's Instagram" width="22px" src="https://raw.githubusercontent.com/hussainweb/hussainweb/main/icons/instagram.png" />
</a>
<a href="https://twitter.com/AngeloCasell">
  <img align="left" alt="Abhishek Naidu | Twitter" width="22px" src="https://raw.githubusercontent.com/peterthehan/peterthehan/master/assets/twitter.svg" />
</a>
<a href="https://www.linkedin.com/in/castilloperz/">





