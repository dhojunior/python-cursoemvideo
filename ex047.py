print('-=-' * 12)
print('{:^36}'.format('DESAFIO 047'))
print('-=-' * 12)
'''for c in range(1, 51):
    if c % 2 == 0:
        print(c)
print('Fim')'''
# Correção Guanabara
for n in range(2, 51, 2): #Ocupa menos memória, exige menos da máquina!
    print(n, end=' ')
print('Acabou')