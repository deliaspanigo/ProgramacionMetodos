# # # # TP 01
# # # # Problema 04
# Problema 4: Escriba un programa que ingrese los coeficientes A, B y C de un polinomio real de segundo
# grado (Ax2 + Bx + C), calcule e imprima en pantalla las dos ra´ıces del polinomio en formato complejo
# x + iy.


# Librerias
import math as math

def RaicesParabola(A, B, C, decimales = 4): #def para que sea funcion. Parametros entre()


    # Armado simbolico del polinomio 
    # Signos para ecuacion
    signoA = "+"
    signoB = "+"
    signoC = "+"

    if A < 0:
        signoA = ""
    if B < 0:
        signoB = ""
    if C < 0:
        signoC = ""

    # Cambio de valores
    A_mod = A
    B_mod = B
    C_mod = C

    if A == 1:
        A_mod = ""
    if B == 1:
        B_mod = ""
    if C == 0:
        C_mod = ""

    # Partes de cada grado
    grado2 = str(A_mod) + str("x**2")
    grado1 = signoB + str(B_mod) + str("x")
    grado0 = signoC + str(C_mod)

    if A == 0:
        grado2 = ""
    if B == 0:
        grado1 = ""
    if C == 0:
        grado0 = ""


    # Polinomio
    polinomio = str("p(x) = ") + grado2 + str(" ") + grado1 + str(" ") + grado0
    polinomio
        



    # Discriminante y absoluto del discriminante
    discriminante = B**2 - 4*A*C
    abs_discriminante = abs(discriminante)
    dt_reales = discriminante >= 0



    if dt_reales:
        la_raiz =  math.sqrt(discriminante)
    else:
        la_raiz =  math.sqrt(abs_discriminante)


    # Partes de la primera raiz
    r1_parte1 = (-B)/(2*A) 
    r1_parte2 =  la_raiz/(2*A)
    r1_parte1_redondeado = round(r1_parte1, decimales)
    r1_parte2_redondeado = round(r1_parte2, decimales)




    # Partes de la segunda raiz
    r2_parte1 = r1_parte1 
    r2_parte2 = - r1_parte2
    r2_parte1_redondeado = round(r2_parte1, decimales)
    r2_parte2_redondeado = round(r2_parte2, decimales)

    # Si las raices son reales
    if dt_reales:
        r1 = r1_parte1 + r1_parte2
        r2 = r2_parte1 + r2_parte2 # Ya tuebe el signo menos dentro de parte2
        
        # Redondeamos las raices
        r1 = round(r1, decimales)
        r2 = round(r2, decimales)

    # Si las raices son imaginarias
    else:
        r1 = str(r1_parte1_redondeado) + str(" + ") + str(r1_parte2_redondeado) + str("i") 
        r2 = str(r2_parte1_redondeado) + str(" + ") + str(r2_parte2_redondeado) + str("i")

    ####################################################################################################

    # Cantidad de Raices y Orden de las raices
    cantidad_raices = ""
    orden_raices = ""

    if r1 == r2: 
        cantidad_raices = 1
        orden_raices = 2
    else: 
        cantidad_raices = 2
        orden_raices = 1

    #####################################################################################################




    # Salida con texto

    # # Salida General
    print("Polinomio: ", polinomio)

    # Si las raices son reales
    if dt_reales:

        # Si hay solo una raiz
        if cantidad_raices == 1:
            print("El polinomio presenta una raiz real de orden 2")
            print("r1: ", r1)
            print("r2: ", r2)

        else:
            print("El polinomio presenta dos raíces reales, cada una de orden 1")
            print("r1: ", r1)
            print("r2: ", r2)

    else:
        print("El polinomio presenta dos raíces imaginarias, cada una de orden 1")
        print("r1: ", r1)
        print("r2: ", r2)





RaicesParabola(A = 1, B = 0, C = -4, decimales = 4)




