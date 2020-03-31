# -*- coding: utf-8 -*-

from sympy import *
from sympy.plotting import plot
x, y, z, t = symbols('x y z t')
k, m, n = symbols('k m n', integer=True)
f, g, h = symbols('f g h', cls=Function)
init_printing()  

plot(x**2, (x, -5, 5))
# Konsole




