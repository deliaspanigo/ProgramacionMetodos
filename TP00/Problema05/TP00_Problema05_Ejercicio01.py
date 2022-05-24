

# # # # # TP 00
# # # # #  Problema 05
# # Ejercicio 1) 
# En un mismo graafico, sobreponer las siguientes funciones incluyendo su leyenda, ejes, t´ıtulo, y
# usando distintos estilos de trazado.
# Considere el rango de valores para x : 0 < x < 20 con 1000 puntos en este intervalo.
# y1 = cos(x)
# y2 = sin(x)
# y3 = cos(2x)
# y4 = sin(x/2)


# Importamos el modulo numpy
# y le damos de alias npy
# from re import X
import numpy as np
import matplotlib.pyplot as plt
import statistics as stat

# Creamos primero al array "x"
# Con el detalle de que  0 < x < 20 con 1000 puntos
# Como dice 1000 puntos en el intervalo abierto 0 a 20, lo que voy
# a hacer es darle 1002 puntos, y despues quitar el primero y el ultimo
# para quedarme con 1000 puntos dentro del intervalo abierto.

# Creamos a x
x = np.linspace(0, 20, 1002)
x

# Veamos un poco algunas cosas... cuantos datos tiene, cual es su primer valor y ultimo, y su minimo y maximo.

# Cantidad de datos de x
len(x)

# Primer elemento de x
x[0]

# Ultimo elemento de x
x[-1]

# Info de "x"
info_x = [min(x), max(x)]
info_x

# Como 0 y 20 estan incluidos en el array "x", vamos a eliminar el primer elento de "x" y el ultimo
x_mod = np.delete(x, 0) # Eliminamos el primer valor
x_mod = np.delete(x_mod, -1) # Eliminamos el ultimo valor
x_mod

# Info de "x_mod"
info_x_mod = [min(x_mod), max(x_mod), len(x_mod)]
info_x_mod

# Creamos las otras variables con x_mod
y1 = np.cos(x_mod)
y2 = np.sin(x_mod)
y3 = np.cos(2*x_mod)
y4 = np.sin(x_mod/2)


# Graficamos a X_mod e Y
plt.plot(x_mod, y1,'r-',label="Cos(x)")
plt.plot(x_mod, y2, 'b-',label="Sen(x)")
plt.plot(x_mod, y3, 'r--',label="Cos(2x)")
plt.plot(x_mod, y4, 'b--', label="Sen(x/2)")
plt.suptitle('TP00 - Problema 05') # Le damos un main...
plt.xlabel('X') # El label del eje X
plt.ylabel('Y') # El label del eje Y
plt.title('Gráfico 1 \n Problema 5 \n Ejercicio 1') # Le damos un titulo al grafico
plt.legend() # Indicamos que el label de la curva sea puesto como referencias dentro del grafico. Colocará la referencia de la mejor manera posible.
plt.show()

####################################################################################################################################################################

# Ejercicio a) y = 5 sin(2x) con x : −10 < x < 10

# Creamos un array con los valores de x que seran graficados
x =  npy.arange(-10, 10, 0.1)
x

# Resulta que lo que genera el metodo .arange, lo que hace es crear un array, y no una lista.
type(x)

# Dimensiones de x
npy.shape(x)

# Cantidad de datos de x
len(x)


# Primer elemento de x
x[0]

# Ultimo elemento de x
x[-1]

# Minimo de "x"
datos_x = [min(x), max(x)]
datos_x

# Como -10 esta incluido en el array "x", vamos a eliminar el primer elento de "x"
x_mod = npy.delete(x, 0)
x_mod

# Dimensiones de x_mod
npy.shape(x_mod)

# Cantidad de datos de x
len(x_mod)


# Primer elemento de x
x_mod[0]

# Ultimo elemento de x
x_mod[-1]

# Minimo de "x_mod"
datos_x_mod = [min(x_mod), max(x_mod)]
datos_x_mod


# Barbaro... Todo OK.
# Ahora x_mod se encuentra en el rango requerido -10 < x_mod < 10

# Ahora si creamos y1 (por que es y para el ejercicio 1)
y =  5*npy.sin(2*x_mod)
y

# Analizamos un poco a "y"
# Dimensiones de x_mod
npy.shape(y)

# Cantidad de datos de x
len(y)


# Primer elemento de x
y[0]

# Ultimo elemento de x
y[-1]

# Minimo de "y"
datos_y = [min(y), max(y)]
datos_y

# Graficamos a X_mod e Y
plt.plot(x_mod,y)     # Genera el gráfico
plt.suptitle('Gráfico 1 - TP00 - Problema 04') # Le damos un main...
plt.xlabel('X') # El label del eje X
plt.ylabel('Y') # El label del eje Y
plt.title('Gráfico de la Función \n Problema 4 Ejercicio 1') # Le damos un titulo al grafico
plt.grid() # Le sumamos una grilla al grafico
# plt.plot(x,y, label= "y = 5*npy.sin(2*x)")
plt.plot(x_mod,y, label= "y = 5*npy.sin(2*x)") # A la grafica le asignamos un label, propiamente a la cuerva.
plt.legend() # Indicamos que el label de la curva sea puesto como referencias dentro del grafico. Colocará la referencia de la mejor manera posible.
# plt.ion()
plt.show()


