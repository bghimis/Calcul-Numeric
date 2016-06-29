from numpy import matrix, array, transpose
from numpy.linalg import inv

def f1(x, y):
    return x ** 3 + 3 * x * y ** 2 - 5 * x + 1

def df1dx (x, y):
    return 3 * x ** 2 + 3 * y ** 2 - 5

def df1dy (x, y):
    return 6 * x * y

def f2(x, y):
    return y ** 3 + 3 * x ** 2 * y - 5 * y + 4

def df2dx (x, y):
    return 6 * x * y

def df2dy (x, y):
    return 3 * x ** 2 + 3 * y ** 2 - 5

f = (f1, f2)
def calc_f (f, val):
    answ = []
    for i in range(len (f)):
        answ.append (f[i](val[0], val[1]))

    return answ

f_prim = matrix ([[ df1dx, df1dy],
                  [ df2dx, df2dy]])

def calc_f_prim (f_prim, val):
    answ = [[0 for x in range (len(f_prim))] for y in range (len (f_prim))]
    for i in range(len (f_prim)):
        for j in range(len (f_prim)):
            answ[i][j] = f_prim.item(i, j)(val[0], val[1])

    return matrix (answ)

def newton (f, f_prim, x0, n):
    x0 = array (x0)

    for i in range (n):
        f_prim_x0 = calc_f_prim (f_prim, x0)
        inverse = inv (f_prim_x0)
        
        f_x0 = calc_f (f, x0)

        print 'f\' (' + str (x0) + ') = '
        print f_prim_x0, '\n'

        print '(f\' (' + str (x0) + ') ^ (-1)) = '
        print inverse, '\n'
        
        print 'f (' + str (x0) + ') = ', f_x0, '\n'   

        x_i = x0 - transpose (inverse * (transpose (matrix (f_x0))))        
        print 'x(' + str(i + 1) +') = ', x_i, '\n===========================\n'

        x0 = array (x_i)[0]
        

newton (f, f_prim, [0, 1], 2)
    
