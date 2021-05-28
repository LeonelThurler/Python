#!/usr/bin/env python3


from typing import *
import sys

#Ésta función calcula la iteración de Newton-Raphson para la función f(x)=x^2-2 tomando como semilla x y n es la cantidad de iteraciones.------------------------------------------------------
def N(x,n):
 i=0
 res=x
 while i<n:
  res= (res/2)+1/res
  i=i+1
 return res


#En éste ejemplo tomamos x=3 y n=5.---------------------------------
print(N(3,5))
