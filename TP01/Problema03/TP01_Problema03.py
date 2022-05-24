# # # # TP 01
# # # # Problema 03
# Problema 3: Escribir un programa que pida un numero entero y determine si es multiplo de 2 y de 5.


# Importamos los modulos
    import numpy as np


def Multi2y5(x): #def para que sea funcion. Parametros entre()

    # x = 10

    # 
    dt_m2 = x%2 == 0
    dt_m5 = x%5 == 0


    if dt_m2 & dt_m5:
        print("El valor ", x, " es multiplo de 2 y de 5 simultáneamente.")

    elif dt_m2 & ~dt_m5:
        print("El valor ", x, " es multiplo de 2 y no es multiplo de 5.")

    elif ~dt_m2 & dt_m5:
        print("El valor ", x, " es multiplo de 5 y no es multiplo de 2.")

    elif ~dt_m2 & ~dt_m5:
        print("El valor ", x, " no es multiplo de 2 y tampoco es múltiplo de 5.")


# Veamos que pasa
Multi2y5(10)



