
# https://www.youtube.com/watch?v=MlH2GLFYDes
# https://github.com/platzi/algebra-lineal-python/blob/master/09%20-%20Transformaciones%20Lineales%20y%20Descomposicion%20de%20Matrices/Calcular%20autovalores%20y%20autovectores.ipynb

A = []
# %matplotlib notebook

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

X = np.array([[3,2], [4,1]])
print(X)



A1 = np.array([[-10, 10, 0], [28, -1, 0], [0, 0, -(8/3)]])
# A1 = np.array([[3, -2, 5], [4, 1, 0], [-7, -1, 6]])

print(A1)

# Calculo del determinante 
np.linalg.det(A1) 

# Calculemos para esa matriz los autovalores y autovectores
print(np.linalg.eig(A1))


# Nos devuelve un vector con los autovalores y una matriz con los autovectores
autovalores1, autovectores1 = np.linalg.eig(A1)
print(autovalores1)

###################################################################################


A2 = np.array([[-10, 10, 0], [1, -1, -(72)**(1/2)], [(72)**(1/2), (72)**(1/2), -(8/3)]])
print(A2)

# Calculemos para esa matriz los autovalores y autovectores
print(np.linalg.eig(A2))


# Nos devuelve un vector con los autovalores y una matriz con los autovectores
autovalores2, autovectores2 = np.linalg.eig(A2)
print(autovalores2)

#####################################################################################################

A3 = np.array([[-10, 10, 0], [1, -1, (72)**(1/2)], [-(72)**(1/2), -(72)**(1/2), -(8/3)]])
print(A3)

# Calculemos para esa matriz los autovalores y autovectores
print(np.linalg.eig(A3))


# Nos devuelve un vector con los autovalores y una matriz con los autovectores
autovalores3, autovectores3 = np.linalg.eig(A3)
print(autovalores3)


# for i in range(len(autovalores1)):
#     print()
# autovalores1
# autovalores2
# autovalores3


autovalores_todos = [autovalores1, autovalores2, autovalores3]
autovalores_todos

pd.DataFrame(autovalores_todos)