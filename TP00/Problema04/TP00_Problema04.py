

# Importamos el modulo numpy
# y le damos de alias npy
import numpy as npy
import matplotlib.pyplot as plt
import statistics as stat

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


############################################################################################
# Ejercicio 2)

# Usamos los mismos X, pero cambiamos los valores de Y
# Este es otro "y" que esta suplantando al "y" anterior
y2 =  3*npy.log(x_mod*2)
y2

plt.plot(x_mod,y2)     # Genera el gráfico
plt.suptitle('Gráfico 1 - TP00 - Problema 04') # Le damos un main...
plt.xlabel('X') # El label del eje X
plt.ylabel('Y') # El label del eje Y
plt.title('Gráfico de la Función \n Problema 4 Ejercicio 2') # Le damos un titulo al grafico
plt.grid() # Le sumamos una grilla al grafico
# plt.plot(x,y, label= "y = 5*npy.sin(2*x)")
plt.plot(x_mod,y2, label= "y = 3*npy.log(x*2)") # A la grafica le asignamos un label, propiamente a la cuerva.
plt.legend() # Indicamos que el label de la curva sea puesto como referencias dentro del grafico. Colocará la referencia de la mejor manera posible.
# plt.ion()
plt.show()






