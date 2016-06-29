from prettytable import PrettyTable

def f (x):
    if 8 * x - 5 * x ** 3 > 0:
        return ((8 * x - 5 * x ** 3)/3.0) ** (1/3.0)
    else:
        return -(-(8 * x - 5 * x ** 3)/3.0) ** (1/3.0)

pct = [-2, -1, 1, 2]
upct = [0 for x in range (0, len(pct))]
dpct = [0 for x in range (0, len(pct) - 1)]
tpct = [0 for x in range (0, len(pct) - 2)]
ppct = [0 for x in range (0, len(pct) - 3)]

# Un punct
for i in range (0, len(pct)):
    upct [i] = f(pct[i])
    print 'f(' + str (pct[i]).ljust(3) + ') = ' + str (f (pct[i]))

print ''

# Doua puncte
for i in range (0, len(pct) - 1):
    dpct [i] = (upct[i + 1] - upct[i]) / (pct[i + 1] - pct[i])

    string = ''
    for j in range (i, i + 2):
        string += str (pct[j]) + ', '
    
    print 'f(' + string + ') = ' + str(dpct[i])

print ''
    
# Trei puncte
for i in range (0, len(pct) - 2):
    tpct [i] = (dpct[i + 1] - dpct[i]) / (pct[i + 2] - pct[i])

    string = ''
    for j in range (i, i + 3):
        string += str (pct[j]) + ', '
    
    print 'f(' + string + ') = ' + str(tpct[i])

print ''

# Patru puncte
for i in range (0, len(pct) - 3):
    ppct [i] = (tpct[i + 1] - tpct[i]) / (pct[i + 3] - pct[i])

    string = ''
    for j in range (i, i + 4):
        string += str (pct[j]) + ', '
    
    print 'f(' + string + ') = ' + str(ppct[i])

print ''


def polinom (puncte) :
    n = len (puncte)

    valori = [[0 for x in range(n)] for y in range(n)]

    for i in range(n):
        valori[i][0] = f (puncte[i])

    for cnt in range (1, n):
        for i in range (0, n - cnt):
            valori [i][cnt] = (valori[i + 1][cnt - 1] - valori[i][cnt - 1]) / (puncte[i + cnt] - puncte[i])

    print_pretty (valori)

def print_pretty (x):
    p = PrettyTable()
    for row in x:
        p.add_row(row)

    print p.get_string(header=False, border=False)            
            
polinom (pct)
