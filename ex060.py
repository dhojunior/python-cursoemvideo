from math import factorial
n = int(input('Digite o número para saber seu fatorial: '))
'''valor = factorial(n)
print('{}! ='.format(n), end='')
while n > 1:
    print(' {} '.format(n), end='x')
    n -= 1
print(' 1 = {}'.format(valor))'''
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))