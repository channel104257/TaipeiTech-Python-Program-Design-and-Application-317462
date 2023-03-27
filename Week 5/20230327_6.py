import cmath

def printroot(x, n):
    print('\nx', n,' = ', x1.real, sep='', end='')
    
    if x.imag < 0:
        print(' - ', x1.imag , 'j', sep='', end='')
    else:
        print(' + ', x1.imag, 'j', sep='', end='')

a = float(input('a : '))
b = float(input('b : '))
c = float(input('c : '))

x1 = ( (-b) + cmath.sqrt( (b ** 2) - 4 * a * c)) / (2 * a)
x2 = ( (-b) - cmath.sqrt( (b ** 2) - 4 * a * c)) / (2 * a)

n = 1
printroot(x1, n)
n += 1
printroot(x2, n)
