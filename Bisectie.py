def f(x):
    return 64 * x ** 3 + 4 * x - 1

def f_prim (x):
    return 192 * x ** 2 + 4

def bisectie (f, a, b, n, n_max):
    if n == n_max:
        print 'Solutie: c' + str (n) + ' = ' + str ((a + b) / 2.0), '->', a, b,  '\n'
    else:
        c = (a + b) / 2.0
        
        print 'a' + str(n) + ' = ', a
        print 'b' + str(n) + ' = ', b
        print 'c' + str(n) + ' = ', c

        print 'f(' + 'a' + str(n) + ') = ', f(a)
        print 'f(' + 'c' + str(n) + ') = ', f(c), '\n'

        if f(a) * f(c) < 0:
            print 'f(' + 'a' + str(n) + ') * f(' + 'c' + str(n) + ') < 0 =>\n'
            bisectie (f, a, c, n + 1, n_max)
        else:
            print 'f(' + 'a' + str(n) + ') * f(' + 'c' + str(n) + ') > 0 =>\n'
            bisectie (f, c, b, n + 1, n_max)

def newton (f, f_prim, x0, n, n_max):
    if n == n_max:
        print 'Solutie: x' + str(n) + ' = ', x0
    else:

        print 'x' + str(n) + ' =', x0
        print 'f(x'+ str(n) + ') = f(' + str(x0) + ') =', f(x0)
        print 'f\'(x' + str(n) + ') = f\'(' + str(x0) + ') =', f_prim(x0)
        print 'x' + str(n + 1) + ' = ' + str(x0) + ' - ' + str(f(x0)) + '/' + str(f_prim(x0)) + '\n'
        
        x_urm = x0 - f(x0)*1.0/f_prim(x0)
        
        newton (f, f_prim, x_urm, n + 1, n_max)

print 'Bisectie'
bisectie (f, 0, 1, 0, 3)

print 'Newton'
newton (f, f_prim, 0, 0, 2)
