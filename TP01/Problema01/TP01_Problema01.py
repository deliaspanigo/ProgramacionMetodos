# # # # TP 01
# # # # Problema 01
# Problema 1: Escribir una funcion que realice el promedio de tres nuumeros reales. 
# ¿Como generalizarıas esta funcion de modo tal que pueda calcular el promedio de una cantidad N arbitraria de numeros?




# Forma 1: rustica
a = 10
b = 30
c = 40
suma = a + b + c
cantidad = 3
media = suma/cantidad
media
###################################################################################


# Forma 2: una funcion que toma 3 valores...
def Media3Val(x1, x2, x3): #def para que sea funcion. Parametros entre()
    
    suma = x1 + x2 + x3
    cantidad = 3
    media = suma/cantidad

#    print(media) #solo muestra el resultado no sirve para entrada de otro proceso
    return(media)

# Usamos la funcion
Media3Val(x1 = 10, x2 = 30, x3 = 40)

######################################################################################





# Forma 3: una funcion que toma una cantidad "n" de valores y obtener la media...
def Media01(x): #def para que sea funcion. Parametros entre()
    
    # x = [10, 30, 40]
    # Importamos las librerias
    import numpy as np

    # Objetos intermedios
    suma = np.sum(x)
    cantidad = len(x)
    media = suma/cantidad

#    print(media) #solo muestra el resultado no sirve para entrada de otro proceso
    return(media)

# Usamos la funcion
Media01( x = [10, 30, 40, 50, 50, 60])

######################################################################################




# Forma 4: una funcion que toma una cantidad "n" de valores y obtener la media...

# Definicion una nueva funcion para la media
def Media02():

    # Importamos librerias
    import numpy as np

    # Texto de presentacion
    ingreso = input("Ingrese los valores separados por comas (use puntos para separador decimal)") #los valores se almacenan como texto

    # Valores ingresados por el usuario
    metralla = ingreso.split(",") # Separa el string a un array de "n" elementos
    x = np.float_(metralla) # Pasa el string ingresado a float
    
    # Operamos
    suma = np.sum(x)
    cantidad = len(x)
    media = suma/cantidad

    return(media)
 

#probando la función
Media02()

