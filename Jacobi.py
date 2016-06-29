from numpy import dot, identity, transpose, array_equal, matrix
from numpy.linalg import det, eigvals, norm
from math import sin, cos, pi, sqrt, atan, fabs

A = [[5, 3, 2],
     [3, 6, 3],
     [2, 3, 5]]
b = [[1], [2], [3]]
x0 = [[0], [0], [0]]
    
def jacobi (m, b, x0):
    A = matrix(m)
    B = matrix(b)
    At = transpose (A)

    n = len (A)

    print A, '\n', At
    if array_equal(A, At):
        print 'A este simetrica\n'

    for i in range (n - 1):
        print A[0: i + 1][:,: i - n + 1], ' => ', det(A[0: i + 1][:,: i - n + 1])
    print A, ' => ', det(A), '\n'

    eigenvalues = eigvals (A)
    lambda_1 = max (eigenvalues)
    lambda_n = min (eigenvalues)

    sigma_zero = 2.0 / (lambda_1 + lambda_n)
    q_zero = (lambda_1 - lambda_n) / (lambda_1 + lambda_n)
    
    print 'Eigenvalues: ', eigenvalues
    print 'Lambda_1: ', lambda_1
    print 'Lambda_' + str(n)+ ': ', lambda_n
    print 'Sigma_zero: ', sigma_zero
    print 'q_zero: ', q_zero

    x1 = dot (A, x0) + B * sigma_zero
    x_nou = (x1 - x0)

    lhs = dot (A, x_nou)
    rhs = x_nou
    
    norma = 0
    for i in range (len (lhs)):
        norma = norma + lhs[i].item(0) * rhs[i].item(0)

    print 'Norma: ', norma
    print 'Formula: ||x^n - x|| <= q0^n / (1-q0) * sqrt(norma)'

jacobi(A, b, x0)
