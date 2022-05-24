# Importamos los modulos
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statistics
import math

decimales = 4

def fn01(x1,x2,a=3,b=2):
    return (a*x1)-(b*x1*x2)

def fn02(x1,x2,e=3,f=2):
    return (-e*x2)+(f*x1*x2)



def euler2D(fn01, fn02, t0, tf, x1_0, x2_0, h=0.01):
    
    # Cantidad de intervalos y de marcas
    n = int((tf-t0)/h)
    marcas = n + 1

    # Generamos una lista con los tiempos
    t = list(np.linspace(t0, tf, marcas))

    estimados_x1 = [x1_0]
    estimados_x2 = [x2_0]
   
  

    for i in range(len(t)-1):
        anterior_x1 = estimados_x1[i] # Conejos
        anterior_x2 = estimados_x2[i] # Lobos

        pendiente1 = fn01(anterior_x1, anterior_x2) 
        pendiente2 = fn02(anterior_x1, anterior_x2)
        
        nuevo_x1 = anterior_x1 + (pendiente1*h) # Nuevo Conejo a partir del 
        nuevo_x2 = anterior_x2 + (pendiente2*h) # Nuevo Lobo

        estimados_x1.append(nuevo_x1)
        estimados_x2.append(nuevo_x2)

    # Return Exitoso
    return [t, estimados_x1, estimados_x2]




# Objetos necesarios
raices = [[0,0], [1.5, 1.5]]
diferentes_x1_0 = [2, 3, 4,  3]
diferentes_x2_0 = [1, 1, 10, 3]
calculos = list(np.arange(0, len(diferentes_x2_0), 1))


#####################################################################################################################

# Valores para las funciones y automatizacion
t0 = 0
tf = 10
h = 0.0001

# Todos los calculos de Euler
for i in range(len(diferentes_x1_0)):
    calculos[i]  = euler2D(fn01 = fn01, fn02 = fn02, t0 = t0, tf = tf, x1_0 = diferentes_x1_0[i], x2_0 = diferentes_x2_0[i], h = h)

# Es un solo grafico, sobre el que colocamos todas las graficas juntas
fig, ax = plt.subplots(figsize=(16, 6))

titulo_armado = str("Diagrama de Fase - tf=") + str(tf) + str(" - h=") + str(h)
ax.set_xlabel('X1 - Conejos')
ax.set_ylabel('X2 - Lobos')
ax.set_title(titulo_armado)
ax.grid()


# Dibujamos los diagramas de fase
for i in range(len(calculos)):
    armado = "Grafico" + str(i) + " - " + "x1_0 = " + str(diferentes_x1_0[i]) + ", x2_0 = " + str(diferentes_x2_0[i])
    ax.plot(calculos[i][1], calculos[i][2], label= armado, linewidth=4)

# Marcamos las raices
for i in range(len(raices)):
    ax.plot(raices[i][0], raices[i][1], marker="o", color="red", markersize = 13)

ax.legend(loc = 0)
plt.show()

###########################################################################################################################



fig, ax = plt.subplots(figsize = (16, 6), nrows = len(calculos), ncols = 1)
ax.set_title("Serie de Tiempo")
armado1 = "Conejo" 
armado2 = "Lobo"
armado3 = str("Serie de Tiempo - tf=") + str(tf) + str(" - h=") + str(h) 
# ax.set_xlim(0, 3)
# ax.set_ylim(0, 2)

ax[0].set_title(armado3)

# Graficos Temporales
for i in range(len(calculos)):


    ax[i].grid()
    ax[i].set_xlabel('Tiempo') 
    ax[i].set_ylabel('Tamaño Poblacional')

    ax[i].plot(calculos[i][0], calculos[i][1], label = armado1, linewidth = 4)
    ax[i].plot(calculos[i][0], calculos[i][2], label = armado2, linewidth = 4)
    ax[i].legend()

plt.show()



