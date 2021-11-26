print('-=-' * 12)
print('{:^36}'.format('DESAFIO 061'))
print('-=-' * 12)
print('Gerador de PA')
print('-=-' * 12)
primeiro = int(input('Digite o primeiro termo: '))
razão = int(input('Digite a razão: '))
n = 1
valor = primeiro
while n <= 10:
    print('{} -> '.format(valor), end='')
    valor += razão
    n += 1
print('Fim!')
