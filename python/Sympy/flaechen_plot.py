# -*- coding: utf-8 -*-

from sympy import *
from sympy.plotting import plot_implicit
x, y, z, t = symbols('x y z t')
k, m, n = symbols('k m n', integer=True)
f, g, h = symbols('f g h', cls=Function)
init_printing()  

#p1 = plot_implicit(Eq(x**2 + y**2, 5))

p6 = plot_implicit(y > x**2)




