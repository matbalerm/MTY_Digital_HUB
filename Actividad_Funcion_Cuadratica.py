# Databricks notebook source
import math
from math import sqrt

def func(a,b,c):
    if (b**2)-(4*a*c) < 0:
        print('La solución es con números complejos.')
        return
    x1=(-b-math.sqrt((b**2)-(4*a*c)))/(2*a)
    x2=(-b+math.sqrt((b**2)-(4*a*c)))/(2*a)
    print('Las soluciones y argumentos de la ecuación (x1,x2,[a,b,c]) son: ')
    return round(x1,3),round(x2,3),[a,b,c]

y=func(-1,5,6)
y=list(y)
print(y)

import matplotlib as mpl
from matplotlib import pyplot
def funcplot(x):
    return y[2][0]*(x**2)+y[2][1]*x+y[2][2]

r=range(math.ceil(y[0]-30),math.ceil(y[1]+30))
r=list(r)

pyplot.plot(r, [funcplot(i) for i in r])
pyplot.title("Solución gráfica")
pyplot.ylim(-100, 100)
pyplot.xlim(min(y[0],y[1])-20,max(y[0],y[1])+20)
pyplot.axhline(y=0,color='k')
pyplot.axvline(x=0,color='k')
pyplot.plot(y[0],0,'r',marker='o',label=f'x1={y[0]}')
pyplot.plot(y[1],0,'r',marker='o',label=f'x2={y[1]}')
pyplot.legend()

# COMMAND ----------


