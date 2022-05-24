

# # # # # TP 00
# # # # #  Problema 06
# Problema 6: Dados los siguientes vectores:
# x1 = [1, 2, 3, 4, 5] e y1 = [1,2214, 1,4918, 1,8221, 2,2255, 2,7183].
# x2 = [1, 2, 3, 4, 5] e y2 = [3, 9, 19, 33, 51].
# x3 = [1, 2, 3, 4, 5] e y3 = [10,0000, 13,4657, 15,4931, 16,9315, 18,0472].
# a) determinar usando python si yi, (i = 1, 2, 3) es una funci´on exponencial, logarıtmica o potencial.
# Ayuda: realizar gr´aficos usando diferentes escalas en los ejes.



# Importamos los modulos
import numpy as np
import matplotlib.pyplot as plt
import statistics as stat

# Creamos los x e y del problema
x1 = [1, 2, 3, 4, 5] 
x2 = [1, 2, 3, 4, 5]
x3 = [1, 2, 3, 4, 5]

y1 = [1.2214, 1.4918, 1.8221, 2.2255, 2.7183]
y2 = [3, 9, 19, 33, 51]
y3 = [10.0000, 13.4657, 15.4931, 16.9315, 18.0472]


# Creamos un X e Y general para hacer los graficos que quiere que veamos
x_general = np.linspace(1, 5, 500)
y1_general = np.exp(x_general)
y2_general = np.log(x_general)
y3_general = x_general**2.2

#####################################################################################################

# Creamos los graficos de referencia
# Creamos el espacio grafico y la info para cada subgrafico
fig, ax = plt.subplots(figsize=(16, 6),nrows=1, ncols=3)

# La info de cada grafico esta en el objeto "ax"
# Ahora, podemos detallar lo que querramos para cada gráfico por separado.

# Le damos un subtitulo general
plt.suptitle('Gráfico 1 de 4 - TP00 - Problema 06 \n Funciones Generales')

# Grafico 1 de 4
ax[0].plot(x_general, y1_general,'r-',label="y1 = exponencial")
ax[0].set_xlabel('Angulo')
ax[0].set_ylabel('Valor de la función')
#ax[0,0].set_title('Funciones trigonométricas')
ax[0].grid()
ax[0].legend()


# Grafico 2 de 4
ax[1].plot(x_general, y2_general, 'b-',label="y2 = logaritmica")
ax[1].set_xlabel('Angulo')
ax[1].set_ylabel('Valor de la función')
#ax[1,0].set_title('Funciones trigonométricas')
ax[1].grid()
ax[1].legend(loc= 'upper left')

# Grafico 3 de 4
ax[2].plot(x_general, y3_general, 'g-',label="y3 = potencial")
ax[2].set_xlabel('Angulo')
ax[2].set_ylabel('Valor de la función')
#ax[0, 1].set_title('Funciones trigonométricas')
ax[2].grid()
ax[2].legend()

ax_original = ax
# plt.show()

###################################################################################################################


# 1er set de puntos
plt.suptitle('Gráfico 2 de 4 - TP00 - Problema 06 \n Set 1 de datos')
ax = ax_original
ax[0].scatter(x1, y1, c='red')
ax[1].scatter(x1, y1, c='red')
ax[2].scatter(x1, y1, c='red')
plt.show()

###################################################################################################################

# 2do de puntos
plt.suptitle('Gráfico 3 de 4 - TP00 - Problema 06 \n Set 2 de datos')
ax = ax_original
ax[0].scatter(x2, y2, c='red')
ax[1].scatter(x2, y2, c='red')
ax[2].scatter(x2, y2, c='red')
plt.show()


##################################################################################################################
# 3# do de puntos
plt.suptitle('Gráfico 4 de 4 - TP00 - Problema 06 \n Set 3 de datos')
ax = ax_original
ax[0].scatter(x3, y3, c='red')
ax[1].scatter(x3, y3, c='red')
ax[2].scatter(x3, y3, c='red')
plt.show()