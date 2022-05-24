

# # # # # TP 00
# # # # #  Problema 05
# # Ejercicio 2) 
# En una misma figura, realizar 4 graficos (separados), usando la funcion subplot con las siguientes
# funciones. En cada grafico incluir rotulo de los ejes, tıtulo y grilla.
# Considere el rango de valores para x : −5,0 < x < 5,0 con 500 puntos en este intervalo.
# a) y1 = − sin(x) cos(x2)
# b) y2 = sin2(x) cos2(x2)
# c) y3 = exp(−x/4) sin(x)
# d) y4 = exp(−x/2) sin2(x)

# Importamos el modulo numpy
# y le damos de alias npy
# from re import X
import numpy as np
import matplotlib.pyplot as plt
import statistics as stat

# Creamos primero al array "x"
# Con el detalle de que  −5,0 < x < 5,0 con 500 puntos
# Como dice 500 puntos en el intervalo abierto -5 a 5, lo que voy
# a hacer es darle 502 puntos, y despues quitar el primero y el ultimo
# para quedarme con 500 puntos dentro del intervalo abierto.

# Creamos a x
x = np.linspace(-5, 5, 502)
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


# Vamos a simplificar un poco todo...
# vamos a colocar "x_mod" en "x" directamente
x = x_mod

# Creamos las otras variables con x_mod
y1 = -np.sin(x)*np.cos(x**2)
y2 = (np.sin(x)**2)*(np.cos(x**2)**2)
y3 = np.exp(-x/4)*np.sin(x)
y4 = np.exp(-x/2)*np.sin(x)**2


# Creamo un espacio grafico vacio que contendra a un grilla.
# Cada espacio de la grilla contendra 1 grafico.
# La metodo plt.subplots() crea: un grafico vacio general, y separa la inforamcion de cada uno de esos subgraficos.
# El espacio grafico sera subdividido pensadolo como una matriz en filas y columnas.
# Los subgraficos se indican como una matrix, por lo tanto deteallaremos una cantidad de filas y columnas.

# Creamos el espacio grafico y la info para cada subgrafico
fig, ax = plt.subplots(figsize=(16, 6),nrows=2, ncols=2)

# La info de cada grafico esta en el objeto "ax"
# Ahora, podemos detallar lo que querramos para cada gráfico por separado.

# Grafico 1 de 4
ax[0,0].set_xlabel('Angulo')
ax[0,0].set_ylabel('Valor de la función')
#ax[0,0].set_title('Funciones trigonométricas')
ax[0,0].grid()
ax[0,0].plot(x, y1,'r-',label="y1 = -sin(x) cos(x^2)")
ax[0,0].legend()

# Grafico 2 de 4
ax[1,0].set_xlabel('Angulo')
ax[1,0].set_ylabel('Valor de la función')
#ax[1,0].set_title('Funciones trigonométricas')
ax[1,0].grid()
ax[1,0].plot(x, y2, 'b-',label="y2 = npy.sin^2(x)*npy.cos**2(x^2)")
ax[1,0].legend(loc= 'upper left')

# Grafico 3 de 4
ax[0, 1].set_xlabel('Angulo')
ax[0, 1].set_ylabel('Valor de la función')
#ax[0, 1].set_title('Funciones trigonométricas')
ax[0, 1].grid()
ax[0, 1].plot(x, y3, 'g-',label="y3 = exp(-x/4)*npy.sin(x)")
ax[0, 1].legend()

# Grafico 4 de 4
ax[1, 1].set_xlabel('Angulo')
ax[1, 1].set_ylabel('Valor de la función')
#ax[1, 1].set_title('Funciones trigonométricas')
ax[1, 1].grid()
ax[1, 1].plot(x, y4, 'k-', label="y4 = exp(-x/2)*npy.sin2(x)")
ax[1, 1].legend()


# Veamos el grafico
plt.show()




