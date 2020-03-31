// f an der Stelle (2,4) auswerten
f = x1 + x2**2
repl = [(x1,2),(x2,4)]
a = f.subs(repl)
print(a)


// Mit Rational bleiben die Brüche
f = x1 + 2*x2*x3 + x4**3/3
repl1 = [(x1,Rational(1,2)),(x2,1),(x3,-1),(x4,2)]
a = f.subs(repl1)
print(a)

repl2 = [(x1,Rational(1,2)+Rational(1,5)*h),(x2,1-Rational(2,5)*h),(x3,-1+Rational(2,5)*h),(x4,2+Rational(4,5)*h)]
b = f.subs(repl2)
b = simplify(b)

print(b-a)
