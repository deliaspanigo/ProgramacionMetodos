# # # # TP 01
# # # # Problema 02
# Problema 2: Escribir un programa que pida dos numeros reales e imprima en la pantalla el mayor de
# ellos. El programa debe indicar si los numeros son iguales.




# Forma 1: rustica
a = 20
b = 20

if a == b:
    print("Ambos valores son iguales a ", a)
elif a > b:
    print("El mayor valor es a: ", a)
    
elif a < b:
    print("El mayor valor es b: ", b)
###################################################################################


# Forma 2: una funcion que toma 2 valores...
def MaxDe2Valores(x1, x2): #def para que sea funcion. Parametros entre()
    if x1 == x2:
        maximo = x1
        print("Ambos valores (x1 y x2) son iguales a ", maximo)

    elif x1 > x2:
        maximo = x1
        print("El mayor valor es a: ", maximo)
    
    elif x1 < x2:
        maximo = x2
        print("El mayor valor es a: ", maximo)

#   print(media) #solo muestra el resultado no sirve para entrada de otro proceso
    return(maximo)

# Usamos la funcion
MaxDe2Valores(x1 = 10, x2 = 30)

######################################################################################





# Forma 3: una funcion que toma una cantidad "n" de valores y devuelve el maximo...
def Maximo01(x): #def para que sea funcion. Parametros entre()
    
    #x = [10, 30, 40]

    # Calculamos el maximo del array ingresado
    maximo = max(x)
    # maximo

    # Determinamos la longitud del array
    cantidad_total = len(x)
    # cantidad_total


    # Determinamos para cada objeto si es igual o no al maximo
    dt_iguales = np.array(x) == maximo
    # dt_iguales

    # Pasamos los valores logicos a 0 y 1 como numeros
    numericos_iguales = dt_iguales.astype(int)


    # Sumamos para determinar cuantos valores son iguales al maximo
    cantidad_iguales = sum(numericos_iguales)  




    # Si solo hay un valor de entrada
    if cantidad_total == 1:
        print("El valor máximo es: ", maximo)

    # Si hay dos o mas valores en la entrada
    elif cantidad_total >= 2:

        # Si no todos los valores son iguales...
        if cantidad_iguales < cantidad_total:
            print("El valor máximo es: ", maximo)

        else:
            print("Todos los valores son iguales. El valor máximo es: ", maximo)


    return(maximo)


Maximo01(x = [30, 30, 30])

######################################################################################




