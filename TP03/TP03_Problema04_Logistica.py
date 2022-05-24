# # # # TP 03
# # # # Problema 04
# Problema 4:  Ecuacion logistica
# Intervalo de tiempo [0, 50]
# Delta t = 0.1
# Considerar 5 condiciones iniciales: N0 = [0, 2, 50, 120, 200]


# Importamos los modulos
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statistics
import math


# Establecemos valores generales
decimales = 4



# Definicion de f()
# Esto es una funcion que otorga la la velocidad de crecimiento
# que es la ecuacion logistica 
def fn4(r, K, N): 
    derivada =  r*N*(1-(N/K)) # Ingresar la función
    return derivada # Devolvemos la derivada para el par t,x


def EuLeR04(fx, r, K, N0, t0, tf, delta):
    
    # Cantidad de intervalos
    n = int((tf-t0)/delta)

    # Inicializamos a "t" y a "poblacion"
    poblacion = [N0]
    t = [t0]
    

    # Ingreamos a un bucle for... 
    # Armamos una lista con los sucesivos tiempos
    for i in range(n):
        tiempo_anterior = t[i]
        nuevo_tiempo = tiempo_anterior + delta 
        t.append(nuevo_tiempo) # Nuevo tiempo

    for i in range(n):
        punto_anterior = poblacion[i]
        pendiente = fx(r = r, K = K, N = punto_anterior)
        punto_nuevo = punto_anterior + pendiente*delta # Aproximacion de Euler
        poblacion.append(punto_nuevo)

    # Return Final    
    return t, poblacion

# Inputs generales
t0 = 0
tf = 50
r = 2
K = 100
delta = 0.1
diferentes_N0 = [0, 2, 50, 120, 200]


# Estimaciones de crecimiento poblacional logistico para direntes condiciones iniciales
t1, p1 = EuLeR04(fx = fn4, r = r, K = K, N0 = diferentes_N0[0], t0 = t0, tf = tf, delta = delta)

t2, p2 = EuLeR04(fx = fn4, r = r, K = K, N0 = diferentes_N0[1], t0 = t0, tf = tf, delta = delta)

t3, p3 = EuLeR04(fx = fn4, r = r, K = K, N0 = diferentes_N0[2], t0 = t0, tf = tf, delta = delta)

t4, p4 = EuLeR04(fx = fn4, r = r, K = K, N0 = diferentes_N0[3], t0 = t0, tf = tf, delta = delta)

t5, p5 = EuLeR04(fx = fn4, r = r, K = K, N0 = diferentes_N0[4], t0 = t0, tf = tf, delta = delta)


# Grafico
fig, ax = plt.subplots(figsize=(15, 5))
ax.set_xlabel('Tiempo')
ax.set_ylabel('Tamanio Poblacional')
ax.set_title('Crecimiento Poblacional Logístico')
# ax.set_xlim(0, 3)
# ax.set_ylim(0, 2)
ax.grid()
ax.plot(t1, p1,'r', label= "N0 = 0")
ax.plot(t2, p2,'g', label= "N0 = 2")
ax.plot(t3, p3,'b', label= "N0 = 50")
ax.plot(t4, p4,'k', label= "N0 = 120")
ax.plot(t5, p5,'orange', label= "N0 = 200")

ax.legend()
plt.show()


