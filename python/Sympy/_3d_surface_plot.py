# -*- coding: utf-8 -*-

from sympy import *
from sympy.plotting import plot3d
x, y, z, t = symbols('x y z t')
k, m, n = symbols('k m n', integer=True)
f, g, h = symbols('f g h', cls=Function)
init_printing()  

plot3d(x*y, (x, -5, 5), (y, -5, 5))

# default bereich ist zwischen -10 und 10
#plot_parametric((cos(x), sin(x)), (x, cos(x)))

# mehrere parametrische plotte
# plot_parametric((cos(x), sin(x), (x, -5, 5)),(cos(x), x, (x, -5, 5)))




