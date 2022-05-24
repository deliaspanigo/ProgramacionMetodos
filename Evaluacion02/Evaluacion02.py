
# Evaluacion02
# Alumno: David Elias Panigo
###########################################

#% matplotlib inline
#% matplotlib notebook

###########################################################################################
# Importamos los modulos
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statistics
import math

decimales = 4

def fn01(x,y):
    derivada1 = 10*(y - x)
    return derivada1

def fn02(x, y, z):
    derivada2 = 28*x - y - x*z
    return derivada2


def fn03(x, y, z):
    derivada3 = x*y -(8/3)*z
    return derivada3

def euler3D(fn01, fn02, fn03,t0, tf, x0, y0, z0, h = 0.01):
    
    # Cantidad de intervalos y de marcas
    n = int((tf-t0)/h)
    marcas = n + 1

    # Generamos una lista con los tiempos
    t = list(np.linspace(t0, tf, marcas))

    estimados_x = [x0]
    estimados_y = [y0]
    estimados_z = [z0]
  

    for i in range(len(t)-1):
        anterior_x = estimados_x[i] 
        anterior_y = estimados_y[i] 
        anterior_z = estimados_z[i]

        pendiente1 = fn01(anterior_x, anterior_y) 
        pendiente2 = fn02(anterior_x, anterior_y, anterior_z)
        pendiente3 = fn03(anterior_x, anterior_y, anterior_z)
        
        nuevo_x = anterior_x + (pendiente1*h)  
        nuevo_y = anterior_y + (pendiente2*h)
        nuevo_z = anterior_z + (pendiente3*h)

        estimados_x.append(nuevo_x)
        estimados_y.append(nuevo_y)
        estimados_z.append(nuevo_z)

    # Return Exitoso
    return [t, estimados_x, estimados_y, estimados_z]


def distancia3D(coordenadas3D):
    x = coordenadas3D[0]
    y = coordenadas3D[1]
    z = coordenadas3D[2]

    distancia = [0]

    for k in range(len(x)-1):
        delta_x = x[k+1] - x[k]
        delta_y = y[k+1] - y[k]
        delta_z = z[k+1] - z[k]

        nuevo_segmento = (delta_x**2 + delta_y**2 + delta_z**2)**(1/2) 
        distancia.append(nuevo_segmento)

    return distancia

# Objetos necesarios
raices = [[0,0,0], [math.sqrt(72), math.sqrt(72), 27], [-math.sqrt(72), -math.sqrt(72), 27]]
diferentes_x0 = [0, -1, 1,  3]
diferentes_y0 = [1,  1, 1, -3]
diferentes_z0 = [0,  1, 1,  3]
calculos = list(np.arange(0, len(diferentes_x0), 1))


#####################################################################################################################

# Valores para las funciones y automatizacion
t0 = 0
tf = 50
h = 0.01
# x0 = diferentes_x0[0]
# y0 = diferentes_y0[0]
# z0 = diferentes_z0[0]

# Todos los calculos de Euler
for i in range(len(diferentes_x0)):
    calculos[i]  = euler3D(fn01 = fn01, fn02 = fn02, fn03 = fn03, t0 = t0, tf = tf, x0 = diferentes_x0[i], y0 = diferentes_y0[i], z0 = diferentes_z0[i], h = h)


#########################################################################################################


# Solucion c1)  Grafica la solucion x(t), y(t) y z(t).
armado1 = "x(t)"
armado2 = "y(t)"
armado3 = "z(t)"
armado4 = str("Solucion c1) Serie de Tiempo") + str(' - tf=') + str(tf) + str(' - h=') + str(h) 
fig, ax = plt.subplots(figsize = (16, 6), nrows = 4, ncols = 1)

fig.suptitle(armado4, fontsize=16)

plt.subplots_adjust(top=0.8, wspace=0.5, hspace = 0.8)


# ax[0].set_title(armado4)
ax[0].plot(calculos[0][0], calculos[0][1], label = armado1, linewidth = 4, color = 'b')
ax[0].legend(loc = 0)
ax[0].set_ylabel('x')
ax[0].set_xlabel('Tiempo')

ax[1].plot(calculos[0][0], calculos[0][2], label = armado2, linewidth = 4, color = 'orange')
ax[1].legend(loc = 0)
ax[1].set_ylabel('y')
ax[1].set_xlabel('Tiempo')

ax[2].plot(calculos[0][0], calculos[0][3], label = armado3, linewidth = 4, color = 'g')
ax[2].legend(loc = 0)
ax[2].set_ylabel('z')
ax[2].set_xlabel('Tiempo')

ax[3].plot(calculos[0][0], calculos[0][1], label = armado1, linewidth = 4, c = 'b')
ax[3].plot(calculos[0][0], calculos[0][2], label = armado2, linewidth = 4, c = 'orange')
ax[3].plot(calculos[0][0], calculos[0][3], label = armado3, linewidth = 4, c = 'green')
ax[3].legend(loc = 0)
ax[3].set_xlabel('Tiempo')
plt.show()



########################################################################################################
# Solucion c2) X-Z, X-Y, Z-Y
armado1 = "X-Z"
armado2 = "X-Y"
armado3 = "Z-Y"
armado4 = str("Solucion c2) Relacion de a pares") + str(' - tf=') + str(tf) + str(' - h=') + str(h)
limite = 12
vector_limite = range(limite)

fig, ax = plt.subplots(figsize = (16, 6), nrows = 2, ncols = 2)
fig.suptitle(armado4, fontsize=16)

plt.subplots_adjust(top=0.8, wspace=0.5, hspace = 0.5)

ax[0,0].set_title(armado1)
ax[0,0].plot(calculos[0][1], calculos[0][3], label = armado1, linewidth = 1, c = 'b', zorder = 1)
ax[0,0].legend(loc = 0)
ax[0,0].grid()
ax[0,0].set_xlabel('x')
ax[0,0].set_ylabel('z')
for i in range(len(raices)):
    ax[0,0].scatter(raices[i][0], raices[i][2], c ='r', marker='o', zorder = 2) # ax.scatter(raices, c ='r', marker='o')

ax[0,1].set_title(armado2)
ax[0,1].plot(calculos[0][1], calculos[0][2], label = armado2, linewidth = 1, c = 'orange', zorder = 1)
ax[0,1].legend(loc = 0)
ax[0,1].grid()
ax[0,1].set_xlabel('x')
ax[0,1].set_ylabel('y')
for i in range(len(raices)):
    ax[0,1].scatter(raices[i][0], raices[i][1], c ='r', marker='o', zorder = 2) # ax.scatter(raices, c ='r', marker='o')

ax[1,1].set_title(armado3)
ax[1,1].plot(calculos[0][3], calculos[0][2], label = armado3, linewidth = 1, c = 'green', zorder = 1)
ax[1,1].legend(loc = 0)
ax[1,1].grid()
ax[1,1].set_xlabel('z')
ax[1,1].set_ylabel('y')
for i in range(len(raices)):
    ax[1,1].scatter(raices[i][2], raices[i][1], c ='r', marker='o', zorder = 2) # ax.scatter(raices, c ='r', marker='o')

plt.show()






# Solucion c3) Grafico 3D
armado4 = str("Solucion c3) Grafico 3D- Gráfico 1 de 2") + str(' - tf=') + str(tf) + str(' - h=') + str(h)
fig = plt.figure()
ax = plt.axes(projection="3d")
ax.set_title(armado4, fontsize=16)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.plot3D(calculos[0][1], calculos[0][2], calculos[0][3])
for i in range(len(raices)):
    ax.scatter(raices[i][0], raices[i][1], raices[i][2], c ='r', marker='o') # ax.scatter(raices, c ='r', marker='o')
plt.show()




# Solucion c3) Grafico 3D con colores
armado4 = str("Solucion c3) Grafico 3D- Gráfico 2 de 2") + str(' - tf=') + str(tf) + str(' - h=') + str(h)
fig = plt.figure()
ax = plt.axes(projection="3d")
ax.set_title(armado4, fontsize=16)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.plot3D(calculos[0][1], calculos[0][2], calculos[0][3]) # Todo el espiral
ax.scatter(diferentes_x0[0], diferentes_y0[0], diferentes_z0[0], c ='g', marker='o', s = 100) # Punto inicial
ax.scatter(calculos[0][1][-1], calculos[0][2][-1], calculos[0][3][-1], c ='black', marker='o', s = 100) # Punto final
for i in range(len(raices)):
    ax.scatter(raices[i][0], raices[i][1], raices[i][2], c ='r', marker='o') # Las soluciones del sistema
plt.show()


####################################################################################################




# Solucion D) Parte 1 de 3
tiempo_limite = 12
pos_limite = calculos[0][0].index(12)
armado4 = str("Solucion D) Parte 1 de 3") + str(' - tf=') + str(tiempo_limite) + str(' - h=') + str(h)
fig = plt.figure()
ax = plt.axes(projection="3d")
ax.set_title(armado4, fontsize=16)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
armado1 = "calculo1"
armado2 = "calculo2"
armado3 = "calculo3"
cantidad = len(calculos) - 1
# vector = list(np.arange(1, (cantidad+1), 1))
vector = list(np.arange(1, (cantidad+1), 1))

ax.plot3D(calculos[1][1][0:pos_limite], calculos[1][2][0:pos_limite], calculos[1][3][0:pos_limite], c = "g")
ax.plot3D(calculos[2][1][0:pos_limite], calculos[2][2][0:pos_limite], calculos[2][3][0:pos_limite], c = "r")
ax.plot3D(calculos[3][1][0:pos_limite], calculos[3][2][0:pos_limite], calculos[3][3][0:pos_limite], c = "b")


for j in range(len(raices)):
    ax.scatter(raices[j][0], raices[j][1], raices[j][2], c ='r', marker='o') # Las soluciones del sistema

for i in vector:
    ax.scatter(diferentes_x0[i], diferentes_y0[i], diferentes_z0[i], c ='g', marker='o', s = 100) # Punto inicial
    ax.scatter(calculos[i][1][pos_limite], calculos[i][2][pos_limite], calculos[i][3][pos_limite], c ='black', marker='o', s = 100) # Punto final
plt.show()
###########################################################################################################################


# Solucion D) Parte 2 de 3
fig = plt.figure()
armado4 = str("Solucion D) Parte 2 de 3") + str(' - tf=') + str(tiempo_limite) + str(' - h=') + str(h)
# Creating a subplot where we are
# defining the projection as 3D projection
# armado4 = str("Solucion D) Parte 1 de 2") + str(' - tf=') + str(tiempo_limite) + str(' - h=') + str(h)

posicion = [[2,1,2], [2,2,1], [2,2,2]]
colores = ["g", "r", "b"]
cantidad = len(calculos) - 1
vector = list(np.arange(1, (cantidad+1), 1))

for i in vector:
    armado5 = str("Caso ") + str(i) + str(": Condiciones Iniciales: (x,y,z) = (") + str(diferentes_x0[i]) + "," + str(diferentes_y0[i]) + "," + str(diferentes_z0[i]) + str(")") 

    ax = fig.add_subplot(posicion[i-1][0], posicion[i-1][1],posicion[i-1][2], projection='3d')
    ax.set_title(armado5, fontsize=16)
    # ax.set_title(str(i), fontsize=16)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.plot3D(calculos[i][1][0:pos_limite], calculos[i][2][0:pos_limite], calculos[i][3][0:pos_limite], c = colores[i-1])
    ax.scatter(diferentes_x0[i], diferentes_y0[i], diferentes_z0[i], c ='g', marker='o', s = 100) # Punto inicial
    ax.scatter(calculos[i][1][pos_limite], calculos[i][2][pos_limite], calculos[i][3][pos_limite], c ='black', marker='o', s = 100) # Punto final

    for j in range(len(raices)):
        ax.scatter(raices[j][0], raices[j][1], raices[j][2], c ='r', marker='o') # Las soluciones del sistema
fig.suptitle(armado4, fontsize=16)
plt.show()



###################################################################################################################################


# Solucion D) Parte 3 de 3
#  Grafica la solucion x(t), y(t) y z(t) para otras soluciones
armado1 = "x(t)"
armado2 = "y(t)"
armado3 = "z(t)"
armado4 = str("Solucion D) Parte 3 de 3 - Serie de Tiempo") + str(' - tf=') + str(tf) + str(' - h=') + str(h)
cantidad = len(calculos) - 1
vector = list(np.arange(1, (cantidad+1), 1))


fig, ax = plt.subplots(figsize = (16, 6), nrows = cantidad, ncols = 1)
plt.subplots_adjust(top=0.8, wspace=0.5, hspace = 1.2)
fig.suptitle(armado4, fontsize=16)

# ax[0].set_title(armado4, fontsize=16)

for i in vector:
    armado5 = str("Caso ") + str(i) + str(": Condiciones Iniciales: (x,y,z) = (") + str(diferentes_x0[i]) + "," + str(diferentes_y0[i]) + "," + str(diferentes_z0[i]) + str(")") 
    # ax[i-1].set_title(armado5)
    ax[i-1].set_title(armado5)
    ax[i-1].plot(calculos[i][0], calculos[i][1], label = armado1, linewidth = 4)
    ax[i-1].plot(calculos[i][0], calculos[i][2], label = armado2, linewidth = 4)
    ax[i-1].plot(calculos[i][0], calculos[i][3], label = armado3, linewidth = 4)
    ax[i-1].set_xlabel('Tiempo')
    ax[i-1].legend(loc = 0)
plt.show()


######################################################################################################################
# e) Teniendo en cuenta los resultados de los puntos anteriores... ¿qu´e le ocurre al sistema cuando se
#    inicializa con condiciones levemente diferentes?


######################################################################################################################



h_mod = [0.020, 0.010, 0.005]
calculos_mod = list(np.arange(0, len(h_mod), 1))
valor_fijo = 1
# x0 = diferentes_x0[0]
# y0 = diferentes_y0[0]
# z0 = diferentes_z0[0]

# Todos los calculos de Euler
for i in range(len(h_mod)):
    calculos_mod[i]  = euler3D(fn01 = fn01, fn02 = fn02, fn03 = fn03, t0 = t0, tf = tf, x0 = diferentes_x0[valor_fijo], y0 = diferentes_y0[valor_fijo], z0 = diferentes_z0[valor_fijo], h = h_mod[i])




# Solucion D) Parte 3 de 3
#  Grafica la solucion x(t), y(t) y z(t) para otras soluciones
armado1 = "x(t)"
armado2 = "y(t)"
armado3 = "z(t)"
armado4 = str("Solucion F) Parte 1 de 2 \n Serie de Tiempo para diferentes pasos de ingración (h)") + str(' - tf=') + str(tf) + str("\n") + str("Condiciones Iniciales: (x,y,z) = (") + str(diferentes_x0[valor_fijo]) + "," + str(diferentes_y0[valor_fijo]) + "," + str(diferentes_z0[valor_fijo]) + str(")") 
cantidad_mod = len(calculos_mod)
vector_mod = list(np.arange(1, (cantidad_mod+1), 1))


fig, ax = plt.subplots(figsize = (16, 6), nrows = cantidad_mod, ncols = 1)
plt.subplots_adjust(top=0.8, wspace=0.5, hspace = 1.2)
fig.suptitle(armado4, fontsize=16)

# ax[0].set_title(armado4, fontsize=16)

for i in range(len(calculos_mod)):
    armado5 = str("Caso ") + str(i + 1) + str(" - h=") + str(h_mod[i])
    # ax[i-1].set_title(armado5)
    ax[i].set_title(armado5)
    ax[i].plot(calculos_mod[i][0], calculos_mod[i][1], label = armado1, linewidth = 4)
    ax[i].plot(calculos_mod[i][0], calculos_mod[i][2], label = armado2, linewidth = 4)
    ax[i].plot(calculos_mod[i][0], calculos_mod[i][3], label = armado3, linewidth = 4)
    ax[i].set_xlabel('Tiempo')
    ax[i].legend(loc = 0)
plt.show()



#############



# Solucion D) Parte 2 de 3

coordenadas3D01 = [calculos_mod[0][1][0:pos_limite], calculos_mod[0][2][0:pos_limite], calculos_mod[0][3][0:pos_limite]] 
coordenadas3D02 = [calculos_mod[1][1][0:pos_limite], calculos_mod[1][2][0:pos_limite], calculos_mod[1][3][0:pos_limite]] 
coordenadas3D03 = [calculos_mod[2][1][0:pos_limite], calculos_mod[2][2][0:pos_limite], calculos_mod[2][3][0:pos_limite]] 

distancias01 = distancia3D(coordenadas3D = coordenadas3D01)
distancias02 = distancia3D(coordenadas3D = coordenadas3D02)
distancias03 = distancia3D(coordenadas3D = coordenadas3D03)

suma01 = round(sum(distancias01), 2)
suma02 = round(sum(distancias02), 2)
suma03 = round(sum(distancias03), 2)

distancias_euclideas = [suma01, suma02, suma03]

fig = plt.figure()
# armado4 = str("Solucion F) Parte 2 de 2") + str(' - tf=') + str(tiempo_limite) + str(' - h=')
armado4 = str("Solucion F) Parte 2 de 2 \n Diferentes pasos de ingración (h)") + str(' - tf=') + str(tf)  + str("\n") + str("Condiciones Iniciales: (x,y,z) = (") + str(diferentes_x0[valor_fijo]) + "," + str(diferentes_y0[valor_fijo]) + "," + str(diferentes_z0[valor_fijo]) + str(")") 

# Creating a subplot where we are
# defining the projection as 3D projection
# armado4 = str("Solucion D) Parte 1 de 2") + str(' - tf=') + str(tiempo_limite) + str(' - h=') + str(h)

posicion = [[2,1,2], [2,2,1], [2,2,2]]
colores = ["g", "r", "b"]

for i in range(len(calculos_mod)):
    armado5 = str("Caso ") + str(i+1) + str(": h=") + str(h_mod[i]) + str("\n Distancia Pitagorica Total=") + str(distancias_euclideas[i])

    ax = fig.add_subplot(posicion[i][0], posicion[i][1],posicion[i][2], projection='3d')
    ax.set_title(armado5, fontsize=16)
    # ax.set_title(str(i), fontsize=16)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.plot3D(calculos_mod[i][1][0:pos_limite], calculos_mod[i][2][0:pos_limite], calculos_mod[i][3][0:pos_limite], c = colores[i-1])
    ax.scatter(diferentes_x0[valor_fijo], diferentes_y0[valor_fijo], diferentes_z0[valor_fijo], c ='g', marker='o', s = 100) # Punto inicial
    ax.scatter(calculos_mod[i][1][pos_limite], calculos_mod[i][2][pos_limite], calculos_mod[i][3][pos_limite], c ='black', marker='o', s = 100) # Punto final

    for j in range(len(raices)):
        ax.scatter(raices[j][0], raices[j][1], raices[j][2], c ='r', marker='o') # Las soluciones del sistema
fig.suptitle(armado4, fontsize=16)
plt.show()

#########################################################


print("La distancia recorrida para 0.02 es ", suma01, " Unidades de Longitud")
print("La distancia recorrida para 0.01 es ", suma02, " Unidades de Longitud")
print("La distancia recorrida para 0.005 es ", suma03, " Unidades de Longitud")
