

# # # # # TP 00
# # # # #  Problema 07
# Problema 7: Grafica el polinomio p(x) = 4x**4 − 5x**2 − 2x 
# en el intervalo −10 < x < 10 con paso 0,1.



# Importamos los modulos
import numpy as np
import matplotlib.pyplot as plt
import statistics as stat

# Esta la dejamos, pero no nos sirve
# x = np.linspace(1, 5, 500)

# Armaos el array x, que va desde -10 a 10, pero sin incluir a -10 y 10
x =  np.arange(-10, 10, 0.1)
x = np.delete(x, 0)
x = np.delete(x, -1)
x

#Creamos el array y 
y = 4*x**4 - 5*x**2 - 2*x
y

#####################################################################################################

# Creamos los graficos de referencia
# Creamos el espacio grafico y la info para cada subgrafico
fig, ax = plt.subplots()

# La info de cada grafico esta en el objeto "ax"
# Ahora, podemos detallar lo que querramos para cada gráfico por separado.

# Le damos un subtitulo general
plt.suptitle('Gráfico 1 de 4 - TP00 - Problema 06 \n Funciones Generales')

ax.plot(x, y,'r-', label = "p(x) = 4*x**4 - 5*x**2 - 2*x")

ax.set_xlabel('Angulo')
ax.set_ylabel('Valor de la función')
#ax[0,0].set_title('Funciones trigonométricas')
ax.grid()
ax.legend()
plt.show()








