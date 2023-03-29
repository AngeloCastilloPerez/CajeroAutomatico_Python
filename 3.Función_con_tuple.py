#DEFINIENDO FUNCIÓN CON TUPLAS

#Definiremos una función que seleccione el helado más caro en la lista de la carta de una heladería!
#Para este ejemplo primero definimos la variable precio_helados con los precios de los helado en tuplas

precio_helados = [('Chocolate', 2.5), ('Mocca', 2.0),('Manjarblanco', 1.5), ('Vainilla', 1.5),('Mango',2.2)]

#Una vez finalizada la lista de precios, definimos las función helado_mas_caro:

def helado_mas_caro(lista_precios):
    precio_max = 0
    helado_mas_caro = ''
    
    for helado,precio in lista_precios:
        if  precio>precio_max:
            precio_max=precio
            helado_mas_caro=helado
        else:
            pass
    
    return (helado_mas_caro,precio_max)

helado,precio = helado_mas_caro(precio_helados)

print(f'El helado de mayor precio es {helado} , y cuesta {precio}')

#SALIDA: El helado de mayor precio es Chocolate , y cuesta 2.5
