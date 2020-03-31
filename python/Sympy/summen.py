n = symbols('n')
a = Sum(1/3**n,(n,0,oo)).doit()
print(a)
