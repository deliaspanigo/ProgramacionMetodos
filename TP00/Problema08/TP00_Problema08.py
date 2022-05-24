

# # # # # TP 00
# # # # #  Problema 08
# # # # # Ejercicio 1
# Dados los siguientes polinomios:
# a) f1(x) = x**3 − 6*x**2 − 12*x − 8
# b) f2(x) = x**3 − 8*x**2 + 20*x − 16
# c) f3(x) = x**3 − 5*x**2 − 7*x − 3
# d) f4(x) = x − 2

# Ejercicio A) Grafique cada una de las funciones en el intervalo [0,4]

# Ejercicio B) Use funciones y clases de la librer´ıa numpy de python con vectores de coeficientes de polinomios para
# evaluar las combinaciones lineales:
# a) f1(x) − 2f3(x)
# b) 3f4(x) − f1(x) − 2f2(x)


#############################################################################################

# Importamos los modulos
import numpy as np
import matplotlib.pyplot as plt
import statistics as stat

# Creamos primero al array "x"
# Con el detalle de que  [0,4] tenemos dos opciones.
# Opcion 1) Usar linsptaces como:  np.linspace(0, 4, 1000)
# Opcion 2) Usar arange como: np.arange(-10, 10, 0.1)
# El primero va a partir el intervalo en 1000 pedazos.
# El segundo tomara valores cada 0.1.


# Creamos a x
x = np.linspace(0, 4, 1000)
x


# Info de "x"
info_x = [min(x), max(x), len(x)]
info_x



# Creamos las otras variables con x_mod
y1 = x**3 - 6*x**2 - 12*x - 8
y2 = x**3 - 8*x**2 + 20*x - 16
y3 = x**3 - 5*x**2 - 7*x - 3
y4 = x - 2

fig, ax = plt.subplots(figsize=(16, 6))
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Ejercicio 1 - Funciones polinómicas')
ax.grid()
ax.plot(x, y1,'r-',label="Cos(x)")
ax.plot(x, y2, 'b-',label="Sen(x)")
ax.plot(x, y3, 'r--',label="Cos(2x)")
ax.plot(x, y4, 'b--', label="Sen(x/2)")
ax.legend()
plt.show()



#######################################################################################################################################



from numpy.polynomial.polynomial import polyval as pval
coeff1 = np.array([-8, -12, -6, 1])
coeff2 = np.array([-16, 20, -8, 1])
coeff3 = np.array([-3, -7, -5, 1])
coeff4 = np.array([-2, 1, 0, 0]) 

# Hay que igualar la cantidad de terminos de todos los polinimios.
# El ultimo es grado 1, por eso le tuve que poner 0 y 0 para el grado 3 y 2.

coef_f13 = coeff1 -2*coeff3
coef_f412 = 3*coeff4 - coeff1 - 2*coeff2

y_p1 = pval(x, coef_f13)
y_p2 = pval(x, coef_f412)


fig, ax = plt.subplots(figsize=(16, 6))
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Ejercicio 2 - Combinaciones lineales de polinomios')
ax.grid()
ax.plot(x, y_p1,'r-', label = "Combinación 1")
ax.plot(x, y_p2, 'b-', label = "Combinacion 2")
ax.legend()
plt.show()


