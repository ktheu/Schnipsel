A = Matrix(3,3,[2,-1,8,6,-4,20,-4,2+a,-13])
rr, cc = A.shape    # shape of matrix
r0 = A.row(0)       # 1. Zeile
cl = A.col(-1)      # letzte Spalte
x = A[0,0]          # Element in Zeile 1, Spalte 1

b = Matrix([4,a,4]) # augmentierte Matrix
Ab = A.row_join(b)

R = Ab.rref()[0]    # rref-Form
simplify(A*x)

eye(3)    # 3x2 Identity Matrix
A.inv()   # die Inverse
A.echelon_form()  # Zeilenstufenform

pprint(A)  # pretty print
init_printing()  # dann schön in Konsole
A.nullspace()  # Basis des Kerns
A.eigenvals()  # Eigenvektoren
D.diagonalize()  # diagonalisierbaar

N.(sqrt(5))  # etwas ausrechnen
