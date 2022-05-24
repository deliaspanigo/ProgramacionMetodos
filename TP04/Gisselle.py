# Importamos los modulos
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statistics
import math

def cone(co,lo,a=3,b=2):
    return((a*co)-(b*co*lo))

def lobo(co,lo,e=3,f=2):
    return((-e*lo)+(f*co*lo))



def eulerCL(cone, lobo, t0, tf, co0, lo0):
    
    h=0.01
    T1 = [t0]
    Co = [co0]
    Lo = [lo0]
    t = t0
    co = co0
    lo = lo0
       
    while t<=tf:
        t = t + h
        co = co + (cone(co,lo)*h)
        lo = lo + (lobo(co,lo)*h)
        T1.append(round(t,2))
        Co.append(round(co,3))
        Lo.append(round(lo,3))
    return(T1,Co,Lo)

T1, Co, Lo = eulerCL(cone, lobo, 0.0, 10.0, 2.0, 1.0)


fig, ax = plt.subplots(figsize=(16, 6))

ax.set_xlabel('Conejos')
ax.set_ylabel('Lobos')
ax.grid(True)
ax.set_title('Diagrama de Fases')
ax.plot(Co,Lo)
ax.plot(Co[1],Lo[2],label="co(0)=0.0, lo(0)=0.0")
plt.plot(3/2,3/2, marker="o", label= "PC(3/2,3/2)")
plt.plot(0,0, marker="o", label= "PC(0,0)")

ax.legend(loc = 0)
plt.show()