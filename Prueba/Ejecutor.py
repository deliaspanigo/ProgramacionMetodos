

# Importamos un archivo ".py" que tenemos en la misma carpeta.
# La importacion se hace como un modulo
# Todo lo contenido en el archivo es parte del modulo
import fibo

# Acceso a una de las funciones que estan en el modulo
fibo.fib(1000)

# Acceso a otra de las funciones del módulo
fibo.fib2(100)

# Nombre del modulo
fibo.__name__

# Asigno la funcion "fib" que pertenece al modulo "fibo" a un nuevo objeto llamado "fib_guardado" entonces
# puedo usar directamente la funcion fib_guardado
fib_guardado = fibo.fib
fib_guardado(1000)


######################################################

# Otra forma de importar
# Aqui dice que... de lo que seria el modulo importe solo "fib" y "fib2"
# y esas funciones pueden ser usadas sin tener que llamar al modulo que las contiene.
from fibo import fib, fib2
fib(500)



#####################################################

# Otra forma de importar...
# Importa todas las funciones del modulo directamente, y las funciones pueden ser usadas 
# directamente sin especificar el modulo. El tema es que no queda especificado en el script que
# funciones estaban contenidas en el modulo
from fibo import *
fib(500)

######################################################

# Otra forma de importar...
# Importar el modulo como un alias
# El modulo recibe un apodo basicamente, y lo llamamos por el apodo... el alias
import fibo as fib
fib.fib(500)

#######################################################################

# Otra forma de importar...
# Importar solo una funcion de un modulo, y a esa funcion darle un alias
from fibo import fib as fibonacci
fibonacci(500)

########################################################################################################################

