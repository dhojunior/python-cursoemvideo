print('-=-' * 12)
print('{:^36}'.format('DESAFIO 052'))
print('-=-' * 12)
n = int(input('Digite o número inteiro que quer saber se é primo: '))
mult = 0
for c in range(2, n):
    if n % c == 0:
        print('Múltiplo de {}'.format(c))
        mult += 1
if mult == 0:
    print('É primo')
else:
    print('Tem {} múltiplos acima de 2 e abaixo de {}'.format(mult, n))
