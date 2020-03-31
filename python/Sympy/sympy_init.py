# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 12:46:49 2018

@author: khthe
"""
from sympy import *
x, y, z, t = symbols('x y z t')
k, m, n = symbols('k m n', integer=True)
f, g, h = symbols('f g h', cls=Function)
init_printing()  

f = sqrt(1/x)
a = Integral(f,(x,3,5))  
b = integrate(f,(x,3,5))
print(a,b)
# a kann jetzt in der Konsole ausgegeben werden


