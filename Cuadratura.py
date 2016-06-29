from prettytable import PrettyTable

puncte = [-1.0 / 2, 0, 1.0 / 2]

def polinom (puncte) :
    n = len (puncte)

    valori = [[0 for x in range(n)] for y in range(n)]

    for i in range(n):
        valori[i][0] = 'f(' + str(puncte[i]) + ')'
        
    for cnt in range (1, n):
        for i in range (0, n - cnt):
            valori [i][cnt] = '(' + valori[i + 1][cnt - 1] + ' - ' + valori[i][cnt - 1] + ') / (' + str (puncte[i + cnt] - puncte[i]) + ')'

    print_pretty (valori)

def print_pretty (x):
    p = PrettyTable()
    for row in x:
        p.add_row(row)

    print p.get_string(header=False, border=True)            
            
polinom (puncte)

