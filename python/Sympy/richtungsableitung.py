from sympy import *
f  = symbols('f', cls=Function)
x, y, h = symbols('x y h')

# Ableitung in Richtung (-2,1)
f = x ** 2 * E ** (x*y**2)
repl1 = [(x,x - h*2),(y,y - h)]
fh = f.subs(repl1)
diffquot = (fh-f)/h
b = limit(diffquot,h,0)
print(b)            # die Richtungsableitung
# Auswertung an der Stellen (1,0)
repl2 = [(x,1),(y,0)]
print(b.subs(repl2))
