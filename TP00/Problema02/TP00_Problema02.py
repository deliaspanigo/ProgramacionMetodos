

# Importamos el modulo numpy
# y le damos de alias npy
import numpy as npy

# Creamos una matrix llamada "a"
a = npy.array([[0, 1, 5], [3, 4, -9], [-1, 6, 7]])

# Un array es un tipo de objeto, como si fuera una lista, pero todos los elementos del array deben ser del mismo tipo.
# Es posible cambiarle partes del array si fuera necesario

# Cuando vemos "a" por consulo, podemos ver que las listas ingresadas como parte del array se conformaran
# las filas del array.

# Creamos otros array a partir del primero

# El objeto b... solo tiene el elemento de la fila 2, columna 2
b = a[1,1]
b

# El objeto c... tiene todos los elementos de la fila 1 (todas las columnas)
c = a[0,:]
c

# El objeto d... tiene las filas de la 1 a la 3, solo la columna 2
d = a[0:2,1]
d

# El objeto e... tiene solo elementos contenidos entre la fila 2 a la 4 (detallado como 1:3)
# y dentro de esas filas, solo las columnas 1 a 3 (detallado como 0:2)
e = a[1:3,0:2]
e

# El objeto f... tiene todas las filas, solo la columna 2 (detallado como 1)
f = e[:,1]
f



type(a)