print('-=-' * 12)
print('{:^36}'.format('DESAFIO 050'))
print('-=-' * 12)
soma = 0
par = 0
for c in range(1, 7):
    n = int(input('Digite o {}º número inteiro: '.format(c)))
    if n % 2 == 0:
        soma += n
        par += 1
print('A Soma dos {} números pares é {}'.format(par, soma))
