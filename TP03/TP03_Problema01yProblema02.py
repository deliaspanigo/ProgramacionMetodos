# # # # TP 03
# # # # Problema 01 y Problema 02
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
def fn01(alfa, valores_variable):

    # Para entender mejor...
    # Esta funcion solo tiene un parametro, que lo denominamos alfa.
    # El ejemplo es: la velocidad de crecimiento problacional es igual a alfa por el valor poblacional.
    derivadas = (alfa*valores_variable)
    return(derivadas)





############################################################################################################

# # # Estimacion de F(x)
# Hacemos un acercamiento a la funcion a partir del metodo de EULER
def EuLeR(t0, tk, particiones, valor_inicial, fx, parametros_fx):

    # Objetos relacionados al tiempo
    marcas = particiones + 1
    tiempo = np.linspace(t0, tk, marcas)
    delta_t = tiempo[1] - tiempo[0]

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
            pendiente = fx(parametros_fx[0], anterior) # Calculamos el valor de la derivada en el punto anterior
            nuevo = anterior + pendiente*delta_t # Hacemos la estimacion para el nuevo punto
            estimados.append(nuevo) # Agregamos la nueva estimacion a la lista
    
    # Return Exitoso
    return(estimados)


################################################################################################################


# Objetos relacionados al tiempo
t0 = 0 # Tiempo inicial
tk = 5 # Tiempo Final
rango = tk - t0 

particiones01 = 100
marcas01 = particiones01 + 1
tiempo01 = np.linspace(t0, tk, marcas01)
delta_t01 = tiempo01[1] - tiempo01[0]

particiones02 = 200
marcas02 = particiones02 + 1
tiempo02 = np.linspace(t0, tk, marcas02)
delta_t02 = tiempo02[1] - tiempo02[0]

particiones03 = 2000
marcas03 = particiones03 + 1
tiempo03 = np.linspace(t0, tk, marcas03)
delta_t03 = tiempo03[1] - tiempo03[0]


# Parametros de la funcion
alfa = 2 # Tasa de crecimiento instantanea

# Valor inicial
valor_inicial = 1


# Valores de la funcion real
data01 = valor_inicial*(np.exp(alfa*tiempo01))   #np.exp() es exponencial con "e" como base
data02 = valor_inicial*(np.exp(alfa*tiempo02))   #np.exp() es exponencial con "e" como base
data03 = valor_inicial*(np.exp(alfa*tiempo03))   #np.exp() es exponencial con "e" como base

# Valores aproximados por funciones diferenciales con Euler
aproximados_euler01 = EuLeR(t0 = t0, tk = tk, particiones = particiones01, valor_inicial = valor_inicial,
                            fx = fn01, parametros_fx = parametros)

# Valores aproximados por funciones diferenciales con Euler
aproximados_euler02 = EuLeR(t0 = t0, tk = tk, particiones = particiones02, valor_inicial = valor_inicial,
                            fx = fn01, parametros_fx = parametros)

# Valores aproximados por funciones diferenciales con Euler
aproximados_euler03 = EuLeR(t0 = t0, tk = tk, particiones = particiones03, valor_inicial = valor_inicial,
                            fx = fn01, parametros_fx = parametros)



# Residuos
residuos01 = data01 - aproximados_euler01
residuos02 = data02 - aproximados_euler02
residuos03 = data03 - aproximados_euler03




# Creamos el espacio grafico y la info para cada subgrafico
fig, ax = plt.subplots(figsize=(16, 6),nrows=2, ncols=3)

# La info de cada grafico esta en el objeto "ax"
# Ahora, podemos detallar lo que querramos para cada gráfico por separado.


minimo_general_x = min(min(tiempo01), min(tiempo02), min(tiempo03))

maximo_general_x = max(max(tiempo01), max(tiempo02), max(tiempo03))


maximo_general_y = max(max(data01), max(data02), max(data03), 
                        max(aproximados_euler01), max(aproximados_euler02), max(aproximados_euler03),
                        max(residuos01), max(residuos02), max(residuos03))

minimo_general_y = min(min(data01), min(data02), min(data03), 
                        min(aproximados_euler01), min(aproximados_euler02), min(aproximados_euler03),
                        min(residuos01), min(residuos02), min(residuos03))


# Grafico 0-0
ax[0,0].set_title(str(particiones01) + " particiones")
ax[0,0].set_xlabel('Tiempo')
ax[0,0].set_ylabel('Tamanio de la Poblacion')
ax[0,0].grid()
ax[0,0].plot(tiempo01, data01, 'r-', color = "orange", label="Función Real Exponencial")
ax[0,0].plot(tiempo01, aproximados_euler01, color = "blue", label = "Método de Euler")
ax[0,0].set_xlim([minimo_general_x, maximo_general_x])
ax[0,0].set_ylim([minimo_general_y, maximo_general_y])
ax[0,0].legend()

# Grafico 1-0
ax[1,0].set_xlabel('Tiempo')
ax[1,0].set_ylabel('Tamanio de la Poblacion')
ax[1,0].grid()
ax[1,0].plot(tiempo01, residuos01, 'b-', color = "red", label = "Residuos")
ax[1,0].set_xlim([minimo_general_x, maximo_general_x])
ax[1,0].set_ylim([minimo_general_y, maximo_general_y])
ax[1,0].legend()

###############################################################################


# Grafico 0-1
ax[0,1].set_title(str(particiones02) + " particiones")
ax[0,1].set_xlabel('Tiempo')
ax[0,1].set_ylabel('Tamanio de la Poblacion')
ax[0,1].grid()
ax[0,1].plot(tiempo02, data02, 'r-', color = "orange", label="Función Real Exponencial")
ax[0,1].plot(tiempo02, aproximados_euler02, color = "blue", label = "Método de Euler")
ax[0,1].set_xlim([minimo_general_x, maximo_general_x])
ax[0,1].set_ylim([minimo_general_y, maximo_general_y])
ax[0,1].legend()

# Grafico 1-1
ax[1,1].set_xlabel('Tiempo')
ax[1,1].set_ylabel('Tamanio de la Poblacion')
ax[1,1].grid()
ax[1,1].plot(tiempo02, residuos02, 'b-', color = "red", label = "Residuos")
ax[1,1].set_xlim([minimo_general_x, maximo_general_x])
ax[1,1].set_ylim([minimo_general_y, maximo_general_y])
ax[1,1].legend()

###############################################################################


# Grafico 0-2
ax[0,2].set_title(str(particiones03) + " particiones")
ax[0,2].set_xlabel('Tiempo')
ax[0,2].set_ylabel('Tamanio de la Poblacion')
ax[0,2].grid()
ax[0,2].plot(tiempo03, data03, 'r-', color = "orange", label="Función Real Exponencial")
ax[0,2].plot(tiempo03, aproximados_euler03, color = "blue", label = "Método de Euler")
ax[0,2].set_xlim([minimo_general_x, maximo_general_x])
ax[0,2].set_ylim([minimo_general_y, maximo_general_y])
ax[0,2].legend()

# Grafico 1-2
ax[1,2].set_xlabel('Tiempo')
ax[1,2].set_ylabel('Tamanio de la Poblacion')
ax[1,2].grid()
ax[1,2].plot(tiempo03, residuos03, 'b-', color = "red", label = "Residuos")
ax[1,2].set_xlim([minimo_general_x, maximo_general_x])
ax[1,2].set_ylim([minimo_general_y, maximo_general_y])
ax[1,2].legend()

###############################################################################

# Veamos el grafico
plt.show()