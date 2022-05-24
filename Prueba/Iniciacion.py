# Pagina
# https://docs.python.org/es/3/tutorial/introduction.html#numbers


# Creamos un objeto con las letras de Python
word = 'Python'
word

# Ingresamos al primer valor (empeiza en cero!)
word[0]

# Ingresamos al segundo elemento del string (que es uno!)
word[1]


# Desde la posicion inicial hasta la posicion 2, sin incluir la posicion 2
word[0:2]


# Desde el inicio hasta la posicion 2 (exluyendo la posicon 2)
word[:2]

# Desde la posicion 4 (incluido) hasta el fina
word[4:]

# Comenzando desde el final, desde el segundo hasta el ultimo
word[-2:]

# No es posible modificar un string.
# No es posible agregarle al objeto word nada, ni modificar su contendio
word[4]

# word[4] <- "A" # Da error
###########################################################################



# cargamos el modulo de funciones matematicas
import math

# Calculamos el coseno
math.cos(math.pi / 4)

# Calculamos el logaritmo en base 2
math.log(1024, 2)


############################################################################

# Eleccion al azar
import random
random.choice(['apple', 'pear', 'banana'])

random.sample(range(100), 10)   # sampling without replacement

random.random()    # random float

random.randrange(6)    # random integer chosen from range(6)



################################################################################


import statistics
data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
statistics.mean(data)

statistics.median(data)

statistics.variance(data)


