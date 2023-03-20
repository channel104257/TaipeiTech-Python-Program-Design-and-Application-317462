import cmath

a = float(input('a : '))
b = float(input('b : '))
c = float(input('c : '))

x1 = ( (-b) + cmath.sqrt( (b ** 2) - 4 * a * c)) / (2 * a)
x2 = ( (-b) - cmath.sqrt( (b ** 2) - 4 * a * c)) / (2 * a)

print('\nx1 = ', x1.real, ' + ', x1.imag, 'i', sep='')
print('\nx2 = ', x2.real, ' + ', x2.imag, 'i', sep='')

def printroot(x):
    print('\nx1 = ', x1.real, ' + ', x1.imag, 'i', sep='', end='')
    
    if x1.imag < 0:
        print(' - ', -(x1.imag), 'i', sep='', end=''())
    else:
        print(' + ', x1.imag, 'i', sep='', end='')
