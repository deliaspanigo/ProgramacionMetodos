

# Importamos el modulo numpy
# y le damos de alias npy
import numpy as npy

# Creamos dos array, "a" y "b"
a = npy.array([-2, 3, 6])
b = npy.array([0, -1, 5])

# Dimensiones de la matriz "a"
npy.shape(a)

# Dimensiones de la matriz "b"
npy.shape(b)

# Realizamos tres calculos que pide el ejercicio

# 1 de 3) Calculamos "f"
f = a - b**2
print(f)


# 2 de 3) Calculamos "t"
t = a - 2*b
print(t)


# 3 de 3) Calculamos "z"
z = 4*a + 3*b
print(z)


