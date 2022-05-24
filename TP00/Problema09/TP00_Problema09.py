

# # # # # TP 00
# # # # #  Problema 09
# Determine las ra´ıces de los siguientes polinomios (sugerencia: numpy.roots). 
# Luego grafique cada polinomio en un intervalo adecuado a fin de verificar dichas raıces:
# a) g1(x) = x**3 − 5*x**2 + 2*x + 8
# b) g2(x) = x**2 − 2*x + 2
# c) g3(x) = x**5 − 3*x**4 − 11*x**3 + 27*x**2 + 10*x − 24
# d) g4(x) = x**5 + 3*x**4 − 4*x**3 − 26*x**2 − 40*x − 24

#############################################################################################

# Importamos los modulos
import numpy as np
import matplotlib.pyplot as plt
import statistics as stat

coefg1=[8, 2, -5, 1]
coefg2=[2, -2, 1]
coefg3=[-24, 10, 27, -11, -3, 1]
coefg4=[-24, -40, -26, -4, 3, 1]

# Raices del polinomio 1
raices01 = np.roots(coefg1)
raices01

# Raices del polinomio 2
raices02 = np.roots(coefg2)
raices02

# Raices del polinomio 3
raices03 = np.roots(coefg3)
raices03

# Raices del polinomio 4
raices04 = np.roots(coefg4)
raices04


# Creamos el espacio grafico y la info para cada subgrafico
fig, ax = plt.subplots(figsize=(16, 6),nrows=2, ncols=2)

# La info de cada grafico esta en el objeto "ax"
# Ahora, podemos detallar lo que querramos para cada gráfico por separado.

# Grafico 1 de 4
x1 = np.arange(min(raices01), max(raices01), 0.1)
y1 = pval(x1, coefg1)
ax[0,0].set_xlabel('X')
ax[0,0].set_ylabel('Y')
#ax[0,0].set_title('Funciones trigonométricas')
ax[0,0].grid()
ax[0,0].plot(x1, y1,'r-', label = "g1(x) = x**3 − 5*x**2 + 2*x + 8")
ax[0,0].legend()

# Grafico 2 de 4
x2 = np.arange(min(raices02), max(raices02), 0.1)
y2 = pval(x2, coefg2)
ax[0,1].set_xlabel('X')
ax[0,1].set_ylabel('Y')
#ax[0,0].set_title('Funciones trigonométricas')
ax[0,1].grid()
ax[0,1].plot(x2, y2,'r-', label = "g2(x) = x**2 − 2*x + 2")
ax[0,1].legend()


# Grafico 3 de 4
x3 = np.arange(min(raices03), max(raices03), 0.1)
y3 = pval(x3, coefg3)
ax[1,0].set_xlabel('X')
ax[1,0].set_ylabel('Y')
#ax[0,0].set_title('Funciones trigonométricas')
ax[1,0].grid()
ax[1,0].plot(x3, y3,'r-', label = "g3(x) = x**5 − 3*x**4 − 11*x**3 + 27*x**2 + 10*x − 24")
ax[1,0].legend()



# Grafico 4 de 4
x4 = np.arange(min(raices04), max(raices04), 0.1)
y4 = pval(x4, coefg4)
ax[1,1].set_xlabel('X')
ax[1,1].set_ylabel('Y')
#ax[0,0].set_title('Funciones trigonométricas')
ax[1,1].grid()
ax[1,1].plot(x4, y4,'r-', label = "g4(x) = x**5 + 3*x**4 − 4*x**3 − 26*x**2 − 40*x − 24")
ax[1,1].legend()

# Veamos el grafico
plt.show()


