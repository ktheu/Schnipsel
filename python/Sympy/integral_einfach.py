# -*- coding: utf-8 -*-
from sympy import *
x = symbols('x y z t')
f = symbols('f', cls=Function)
init_printing()

f = sqrt(1/x)
a = Integral(f,(x,3,5))
b = integrate(f,(x,3,5))
print(a,b)

from sympy import *
t, x  = symbols('t x')
f  = symbols('f', cls=Function)

f = ln(t)
a = Integral(f,(t,1,x)).doit()
print(a)

from sympy import *
t, n, x  = symbols('t n x')
f  = symbols('f', cls=Function)
f = t*exp(-t)

b = Integral(f,(t,0,n)).doit()
print(b)

a = Integral(f,(t,0,+oo)).doit()
print(a)
