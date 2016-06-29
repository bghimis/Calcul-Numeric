from numpy import dot, identity, transpose
from math import sin, cos, pi, sqrt, atan, fabs

A = [[4, 3, sqrt(3)],
     [3, 10, - 2 * sqrt (3)],
     [sqrt(3), -2 * sqrt(3), 14]]

def max_diag_princ (A):
    n = len (A)

    maxim = fabs(A[0][1])
    p = 0
    q = 1
    if A[0][1] < 0:
        neg = -1
    else:
        neg = 1
        
    for i in range (0, n):
        for j in range (i + 1, n):
            if maxim < fabs(A[i][j]):
                maxim = fabs(A[i][j])
                p = i
                q = j

                if A[i][j] < 0:
                    neg = -1
                else:
                    neg = 1

    return (maxim, p, q, neg)

def get_T (p, q, n, theta):
    s = sin (theta)
    c = cos (theta)

    i = identity (n)
    i[p][p] = c 
    i[p][q] = -s
    i[q][p] = s
    i[q][q] = c

    return i
    
def rotatii (A):
    maxim, p, q, neg = max_diag_princ (A)
    n = len (A)
    eps = 1e-10

    # Afisare:
    print 'Maxim = ', maxim
    print 'p = ', p
    print 'q = ', q
    print 'neg = ', neg
    # ========
    
    if fabs (maxim - 0) < eps:
        for i in range (n):
            for j in range (n):
                A[i][j] = round (A[i][j], 5)
        
        return A

    if fabs (A[p][p] - A[q][q]) < eps:
        theta = pi / 4.0
    else:
        theta = 1 / 2.0 * atan ((2 * neg * maxim) / (A[p][p] - A[q][q]))

    # Afisare:
    print 'Theta = ', theta
    # ========
        
    T = get_T(p, q, n, theta)
    Tt = transpose (T)
    
    A_nou = dot(dot(Tt, A), T)

    # Afisare:
    print 'Tpq(theta)'
    print T, '\n'
    
    print 'Tpq -transpus- (theta)'
    print Tt, '\n'
    
    print 'A_nou'
    print A_nou, '\n'
    # ========
    
    return rotatii (A_nou)    

print rotatii (A)
