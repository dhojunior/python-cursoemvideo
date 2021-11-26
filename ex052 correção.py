print('-=-' * 12)
print('{:^36}'.format('CORREÇÃO DESAFIO 052'))
print('-=-' * 12)
num = int(input('Digite o número que quer saber se é primo: '))
cont = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[34m', end='')
        cont += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\n\033[mO número {} foi divisível {} vezes'.format(num, cont))
if cont == 2:
    print('Por isso é um número primo!'.format(num))
else:
    print('Por isso Não é um número primo!'.format(num))