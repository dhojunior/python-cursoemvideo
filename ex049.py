print('-=-' * 12)
print('{:^36}'.format('DESAFIO 049'))
print('-=-' * 12)
'''n = int(input('Digite o número que quer saber a tabuada: '))
i = 1
for c in range(n, n * 10 + 1, n):
    print('{} x {:2} = {:2}'.format(n, i, c))
    i += 1'''
# Correção Guanabara
num = int(input('Digite o número para ver sua tabuada: '))
for c in range(1, 11):
    print('{} x {:2} = {:2}'.format(num, c, num * c))
