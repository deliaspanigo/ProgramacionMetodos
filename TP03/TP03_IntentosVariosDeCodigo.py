# # # # TP 03
# # # # Problema 01
# Problema 1: Considera la siguiente ecuacion diferencial ordinaria (EDO) de primer orden:



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
# para cada valor de la poblacion
def fn01(parametros, valores_variable):

    # Para entender mejor...
    # Esta funcion solo tiene un parametro, que lo denominamos alfa.
    # El ejemplo es: la velocidad de crecimiento problacional es igual a alfa por el valor poblacional.
    alfa = parametros[0]
    derivadas = (alfa*valores_variable)
    return(derivadas)



# Parametros de la funcion
alfa = 2

# Objetos nuevos
nombre_fx = "fn01" # Nombre de la funcion
parametros = [alfa] # Una lista con todos los parametros de la funcion
armado = ""
nombre_lista = "parametros"

# Esto es una forma para que sea lo que sea que use como funcion
# y como argumentos de la funcion, yo pueda usarlo dentro de otras funciones
def StrFun(nombre_fx, parametros, nombre_lista = "parametros"): 
    # Armamos el inicio
    armado = ""
    armado = armado + nombre_fx + "("

    # Agregamos los argumentos
    for k in range(len(parametros)):

        # Agregamos la posicion de cada objeto de la lista
        armado = armado + nombre_lista + "[" + str(k) + "]"

        if k < (len(parametros)-1):
            armado = armado + ","
        else:
            armado = armado + ")"
    
    # Return Exitoso
    return(armado)


# Como notas
notas = StrFun(nombre_fx, parametros, nombre_lista)
notas
exec(notas)

# Objetos relacionados al tiempo
t0 = 0 # Tiempo inicial
tk = 5 # Tiempo Final
particiones = 10000
marcas = particiones + 1
rango = tk - t0
tiempo = np.linspace(t0, tk, marcas)
delta_t = tiempo[1] - tiempo[0]

# Parametros de la funcion
alfa = 2 # Tasa de crecimiento instantanea

# Valor inicial
valor_inicial = 1



# Valores observados de la F(x)
data01 = valor_inicial*(np.exp(alfa*tiempo))   #np.exp() es exponencial con "e" como base


############################################################################################################


fx

# # # Estimacion de F(x)
# Hacemos un acercamiento a la funcion a partir del metodo de EULER
def EuLeR(t0, tk, particiones, valor_inicial, fx, parametros_fx, nombre_lista):

    # Objetos relacionados al tiempo
    marcas = particiones + 1
    tiempo = np.linspace(t0, tk, marcas)
    delta_t = tiempo[1] - tiempo[0]

    notas = StrFun(nombre_fx, parametros_fx, nombre_lista)

    # Inicializacion de los estimados
    estimados = []

    # Por cada valor de tiempo...
    for i in range(len(tiempo)):

        # Si es el primer tiempo... 
        if i == 0:
            estimados.append(valor_inicial) # Agremos el valor inicial
        
        # Para otro tiempo que no sea el primero
        else:
            anterior = estimados[i-1]  # Tomamos la estimacion anterior de f(x)
            pendiente = FUN() # Calculamos el valor de la derivada en el punto anterior
            nuevo = anterior + pendiente*delta_t # Hacemos la estimacion para el nuevo punto
            estimados.append(nuevo) # Agregamos la nueva estimacion a la lista

 
plt.plot(tiempo,data01, color="green")
# # plt.xlabel('x')
# plt.ylabel('y')
# plt.title('Lab DLS')
# plt.show()

plt.plot(tiempo,estimados, color="blue")
# plt.xlabel('x')
# plt.ylabel('y')
 #plt.title('Lab DLS')
plt.show()

# data01 

# estimados

residuos = data01 - estimados


plt.plot(tiempo, residuos, color="red")
# plt.xlabel('x')
# plt.ylabel('y')
 #plt.title('Lab DLS')
plt.show()

# errores

sum(errores)