# -*- coding: utf-8 -*-

from sympy import *
x, y, z, t = symbols('x y z t')
k, m, n = symbols('k m n', integer=True)
f, g, h = symbols('f g h', cls=Function)
init_printing()  

f = x**2 + y**2 - 2*x - 4*y + 5
fx = diff(f,x)
print(fx)   # Konsole




