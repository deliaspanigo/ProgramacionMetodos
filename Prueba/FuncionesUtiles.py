# Strings 
 mi_string = "Aver"

 len(mi_string)

 #############################################################

# Listas
mi_lista = [1, 4, 9, 16, 25]
mi_lista

len(mi_lista)


mi_lista.append(216)  # add the cube of 6
mi_lista.append(7 ** 3)  # and the cube of 7
mi_lista

# Podemos anidar listas dentro de otras listas
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a,n]
x

x[0]
x[0][1]

###############################################################

range(5)


#################################################################

def fib(n):    # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

# Now call the function we just defined:
fib(2000)


##############################################################################