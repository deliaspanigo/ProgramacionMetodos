# # # # TP 03
# # # # Problema 03
# Problema 3:  Usando el programa del ejercicio anterior, resolve el problema de valor inicial

# La ecuacion diferencial es:         x. = (t-x)/2  
# En el intervalo [0,3] con x(0) = 1
# Utiliza delta_t igual a  1, 0.5, 0.25 y 0.123.
# Compara el error final en t = 3 en los cuatro casos
# donde x(t) = t - 2 + c*exp(-t/2) con c = 3


# Importamos los modulos
from cmath import log
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statistics
import math


# Establecemos valores generales
decimales = 4



# Definicion de f()
# Esto es una funcion que otorga la la velocidad de crecimiento 
def fn3(t, x): 
    derivada =  (t - x)/2 # Ingresar la función
    return derivada # Devolvemos la derivada para el par t,x


def EuLeR03(fx, x0, t0, tf, delta):
    
    # Cantidad de intervalos
    n = int((tf-t0)/delta)

    # Inicializamos a "t" y a "x"
    t = [t0]
    x = [x0]

    # Ingreamos a un bucle for... 
    # Armamos una lista con los sucesivos tiempos
    for i in range(n):
        tiempo_anterior = t[i]
        nuevo_tiempo = tiempo_anterior + delta 
        t.append(nuevo_tiempo) # Nuevo tiempo

    for i in range(n):
        punto_anterior = x[i]
        pendiente = fx(t[i], punto_anterior)
        punto_nuevo = punto_anterior + pendiente*delta
        x.append(punto_nuevo)

    # Return Final    
    return t, x

# Inputs generales
t0 = 0
tf = 3
delta = [1, 0.5, 0.25, 0.125]


t1, x1 = EuLeR03(fx = fn3, x0 = 1, t0 = 0, tf = 3, delta = delta[0])

t2, x2 = EuLeR03(fx = fn3, x0 = 1, t0 = 0, tf = 3, delta = delta[1])

t3, x3 = EuLeR03(fx = fn3, x0 = 1, t0 = 0, tf = 3, delta = delta[2])

t4, x4 = EuLeR03(fx = fn3, x0 = 1, t0 = 0, tf = 3, delta = delta[3])


fig, ax = plt.subplots(figsize=(15, 5))
ax.set_xlabel('t')
ax.set_ylabel('x')
ax.set_title('Gráfico de la aproximación a la función')
ax.set_xlim(0, 3)
ax.set_ylim(0, 2)
ax.grid()
ax.plot(t1, x1,'r', label= "f(t) c/delta t 1")
ax.plot(t2, x2,'g', label= "f(t) c/delta t 0.5")
ax.plot(t3, x3,'b', label= "f(t) c/delta t 0.25")
ax.plot(t4, x4,'k', label= "f(t) c/delta t 0.125")
ax.legend()
plt.show()
############################################################################################################


# Para la ecuacion tenemos que c = 3 y solo interesa t = 3, entonces... 
# el valor real de la funcion para t = 3 es:
x_real_3 = 3 - 2 + 3*math.exp(-3/2) 


# Separamos la aproximacion de cada metodo para t = 3
x1_3 = x1[t1.index(3)]
x2_3 = x2[t2.index(3)]
x3_3 = x3[t3.index(3)]
x4_3 = x4[t4.index(3)]

# El error porcentual de cada es...
error1_3 = (abs(x1_3 -  x_real_3)/x_real_3)*100
error2_3 = (abs(x2_3 -  x_real_3)/x_real_3)*100
error3_3 = (abs(x3_3 -  x_real_3)/x_real_3)*100
error4_3 = (abs(x4_3 -  x_real_3)/x_real_3)*100

# Redondeos
error1_3 = round(error1_3, decimales)
error2_3 = round(error2_3, decimales)
error3_3 = round(error3_3, decimales)
error4_3 = round(error4_3, decimales)


print("El error porcentual con delta-t de 1: ", error1_3, "%")
print("El error porcentualcon delta-t de 0.5: ", error2_3, "%")
print("El error porcentualon delta-t de 0.25: ", error3_3, "%")
print("El error porcentualcon delta-t de 0.125: ", error4_3, "%")


