# # # # TP 01
# # # # Problema 03
# Problema 3: Escribir un programa que pida un numero entero y determine si es multiplo de 2 y de 5.


# Importamos los modulos
from cmath import log
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statistics
import math
import seaborn as sb

# Redondeo general
decimales = 4

# Importamos los datos
data = pd.read_csv("Firma.csv")
data

# Ordenamos los datos de menor a mayor longitud de onda
data = data.sort_values(by=['Longitud'])

# Vemosque tipo de datos es "data"
type(data)

# Hacemos una deteccion logica de los datos correctos
# Solo debemos usar las filas que tienen valores de longitud de onda 
# menos o iguales a 1000
dt_correctos = data["Longitud"] <= 1000
data = data.loc[dt_correctos, ]

# Separamos las columnas en dos objetos diferentes
longitud = data["Longitud"] # Toma los datos
longitud = longitud.values.tolist() # Pasa el data frame a lista
reflectancia = data["Reflectancia"] # Toma los datos
reflectancia = reflectancia.values.tolist() # Pasa el data frame a lista

############################################################################################################
# a) Graficar la firma espectral.

plt.plot(longitud,reflectancia)
plt.xlabel('Longitud')
plt.ylabel('Reflectancia')
plt.title('Firma Espectral')
plt.show()


############################################################################################################
# b) Calcular cuanto medirıa un sensor ideal en sus bandas centradas en el azul λazul = 490nm y en el
# verde λverde = 555nm, suponiendo un ancho de banda de 10nm.

# Armamos un array, que tiene una fila por cada color de banda
ancho = 10
mitad = ancho/2
mitad = int(mitad)

info = np.array([
    ["azul", 490, "", ""], 
    ["verde", 555, "", ""]])

cantidad_colores = np.shape(info)[0]
nombres_columnas01 = ["Color", "Longitud de onda Marca de Clase", "Minimo", "Maximo"]

for i in range(cantidad_colores):
    marca_clase = int(info[i, 1])
    info[i, 2] = round(marca_clase - mitad, 0)
    info[i, 3] = round(marca_clase + mitad, 0)


info = pd.DataFrame(info, columns = nombres_columnas01)
info 

# Realizaremos estadisticas por cada banda, dentro del rango establecido de minimo y maximo
# Inicializamos al objeto estadisticas
estadisticas = np.array([])

# Estadisticas y grafico por color
for i in range(cantidad_colores):

    # Definimos el minimo y el maximo
    el_minimo = int(info["Minimo"][i])
    el_maximo = int(info["Maximo"][i])
    
    # Detectamos los datos mayores o igual al minimo
    dt_minimo =  np.asarray(longitud) >= el_minimo

    # Detectamos los datos menores o igual o igual al maximo
    dt_maximo =  np.asarray(longitud) <= el_maximo

    # Detectamos los datos que estan en el rango del color
    dt_color = dt_minimo & dt_maximo
    # dt_color

    mini_longitud = np.asarray(longitud)[dt_color]
    mini_reflectancia = np.asarray(reflectancia)[dt_color]


    minimo = round(min(mini_reflectancia), decimales)
    maximo = round(max(mini_reflectancia), decimales)
    media = round(statistics.mean(mini_reflectancia), decimales)
    mediana = round(statistics.median(mini_reflectancia), decimales)
    desvio = round(statistics.stdev(mini_reflectancia), decimales)
    cv = round(desvio/media, decimales)  # ¿Como corrijo esto? **************************************
    cvPorc = str(cv*100) + str("%")
    n_color = np.shape(mini_longitud)[0] #len(mini_longitud)
    error_estandard = round(desvio/math.sqrt(n_color), decimales)
    
    estadisticas_color = [
                        info["Color"][i],
                        minimo, 
                        maximo,
                        media,
                        mediana,
                        desvio,
                        error_estandard, 
                        cv,
                        cvPorc,
                        n_color

                        ]

    # Si es el primer if, creamos el objeto estadisticas
    if i == 0:
        estadisticas = estadisticas_color
    #    fig, ax = plt.subplots(figsize=(16, 6),nrows=1, ncols=2)

    # Si no es la primera vuelta, anexamos las estadistica nuevas a los que ya existe    
    else:
        estadisticas = np.array([estadisticas, estadisticas_color]) #np.vstack([estadisticas, estadisticas_color])


# Nombres de las columnas
nombres_columnas02 = ["Color", "Minimo", "Maximo", "Media", "Mediana", "Desvio", "Error Estandard", "Coef. Var.", "Coef. Var %", "n"]

# Pasamos de Array a Dataframe
estadisticas = pd.DataFrame(estadisticas, columns = nombres_columnas02)
estadisticas 

###################################################################################################################################
#
# c) Usando el resultado del punto anterior calcule la concentacion de Cl-a en el punto usando el modelo OC2S.

tabla_modelos =  np.array([
    ["OCS2S",   "SeaWiFS",  480,           555,     0.2511,     -2.0853,    1.5035,     -3.1747,    -0.3383],
    ["OC3",     "SeaWiFS",  "443>490",     555,     0.2515,     -2.3798,    1.5823,     -0.6372,    -0.5682],
    ["OC3M",    "MODIS",    "443>488",     547,     0.2424,     -2.7423,    1.8017,     0.0015,     -1.2280],
    ["OC4",     "SeaWiFS",  "443>490>510", 555,     0.3272,     -2.9940,    2.7218,     -1.2259,    -0.5683]])


# Nombres de las columnas
nombres_columnas03 = ["Algoritmo", "Sensor", "Lambda blue", "Lambda Green", "a0", "a1", "a2", "a3", "a4"]

# Pasamos de Array a Dataframe
tabla_modelos = pd.DataFrame(tabla_modelos, columns = nombres_columnas03)
tabla_modelos 


# 5 terminos de la ecuacion... Desde a0 hasta a4
modelo_elegido = 0   # El modelo OC2S dice el enunciado, a pesar que las imagenes son de MODIS

a0 = float(tabla_modelos["a0"][modelo_elegido])
a1 = float(tabla_modelos["a1"][modelo_elegido])
a2 = float(tabla_modelos["a2"][modelo_elegido])
a3 = float(tabla_modelos["a3"][modelo_elegido])
a4 = float(tabla_modelos["a4"][modelo_elegido])

coeficientes = [a0, a1, a2, a3, a4]
coeficientes



media_azul = float(estadisticas["Media"][0])
media_verde = float(estadisticas["Media"][1])

cociente = media_azul/media_verde
log_cociente = math.log10(cociente)

tabla01 = np.array([media_azul, media_verde, cociente, log_cociente])

nombres_columnas04 = ["Media Azul", "Media Verde", "Cociente (Azul/Verde)", "log10 del Cociente"]

# Pasamos de Array a Dataframe
# tabla01 = pd.DataFrame(tabla01, columns = nombres_columnas04)
tabla01


potencias = np.arange(0, 5, 1)
parte01 = log_cociente**potencias
parte02 = coeficientes*parte01

sumatoria = sum(parte02)


clorofila_log10_01 = sumatoria

clorofila_01 = 10**clorofila_log10_01
clorofila_01

#################################################################################################################
# d) Si la determinacion de la Cl-a in situ realizada con el metodo fluorometrico arrojo un valor de
# clafluoro = 0,49 mg m−3
# ¿cual es error relativo y el relativo porcentual?
clorofila_insitu = 0.49

# 0.49 ------------ 1 
# 0.86 ----------- x =   (0.86 * 1)/0.49 = 0.86/ 0.49
# 

# Error Relativo  
error_relativo = clorofila_01/clorofila_insitu
error_relativo

# Error porcentual
error_porcentual = error_relativo*100
error_porcentual = round(error_porcentual, decimales)
error_porcentual = str(error_porcentual) + str("%")
error_porcentual


#################################################################################################################

# e) e) Cual es la ventaja de considerar la siguiente expresion en lugar de la ecuacion (1)?
#      log10(Cla) = a0 + R(a1 + R(a2 + R(a3 + Ra4))), (2)
# donde R es el logaritmo en base 10 del cociente entre la reflectancia del azul (numerador) y el verde (denominador)

R = log_cociente
clorofila_log10_02 = a0 + R*(a1 + R*(a2 + R*(a3 + R*a4)))
clorofila_log10_02

clorofila_02 = 10**clorofila_log10_02
clorofila_02


clorofila_log10_01 / clorofila_log10_02


clorofila_01/clorofila_02

